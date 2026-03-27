import os
import glob
import re
import asyncio
from typing import List, Tuple
from google import genai
from google.genai import types

# ---------------------------------------------------------
# Agent Prompts
# ---------------------------------------------------------

AGENT_1_PROMPT = """You are a Logician. Evaluate the provided text for logical consistency, academic rigor, and scholastic neutrality.
Identify any areas where argumentation is weak, contradictory, or relies on logical leaps rather than evidence.
Provide brief, bulleted notes of your findings. Focus only on structure and logic. If the text is perfectly rigorous, simply output "No logical issues found."
"""

AGENT_2_PROMPT = """You are an Objectivity Reviewer. Examine the provided text for injected personal POV, subjective language (e.g., "I think", "my perspective", "our framework"), and non-academic commentary that an AI assistant might have added inappropriately. 
Provide brief, bulleted notes identifying the problematic phrases or sections. If the text is perfectly objective, simply output "No subjective POV found."
"""

AGENT_3_PROMPT = """You are an Academic Editor. You are given an HTML snippet from an academic deep-dive, along with critique notes from a Logician and an Objectivity Reviewer.
Your task is to REWRITE the English text inside the HTML to fix the logical leaps and comprehensively remove ALL personal point-of-view, subjective injections, or AI-assistant commentary.

CRITICAL RULES:
1. Do NOT alter any HTML tags, classes, structural elements, SVG diagrams, or hyperlinks.
2. Only rewrite the textual content described inside the HTML to be more scholarly, objective, and logically rigorous.
3. If the critiques say "No issues found", just return the exact original HTML.
4. Output ONLY the valid HTML snippet. Do NOT wrap it in markdown block quotes (e.g. ```html ... ```). Output exactly the raw text that should replace the original snippet.
"""

# ---------------------------------------------------------

def extract_js_string_elements(array_text: str) -> List[str]:
    # Extracts contents between backticks carefully, accounting for potential escaping
    # However, a simpler split works for standard read-aid template structure.
    # We will use regex to find all matches of ` ... `
    matches = re.finditer(r'`(.*?)`', array_text, flags=re.DOTALL)
    elements = []
    for m in matches:
        elements.append(m.group(1))
    return elements

def reconstruct_array_text(elements: List[str]) -> str:
    # Reconstructs the inside of the array
    joined = ",\n\n  ".join([f"`{el}`" for el in elements])
    return f"\n  {joined}\n"

async def process_element(client: genai.Client, html_snippet: str) -> Tuple[str, str, str]:
    if not html_snippet.strip():
        return html_snippet, "", ""
    
    max_retries = 10
    for attempt in range(max_retries):
        try:
            # Run Agent 1 & Agent 2 sequentially to lower burst RPM
            res1 = await client.aio.models.generate_content(
                model='gemini-2.5-flash',
                contents=f"Text to evaluate:\n\n{html_snippet}",
                config=types.GenerateContentConfig(system_instruction=AGENT_1_PROMPT, temperature=0.1)
            )
            await asyncio.sleep(2)
            
            res2 = await client.aio.models.generate_content(
                model='gemini-2.5-flash',
                contents=f"Text to evaluate:\n\n{html_snippet}",
                config=types.GenerateContentConfig(system_instruction=AGENT_2_PROMPT, temperature=0.1)
            )
            await asyncio.sleep(2)
            
            logician_notes = res1.text
            pov_notes = res2.text
            
            # Run Agent 3
            agent_3_input = f'''
            ORIGINAL HTML SNIPPET:
            {html_snippet}

            LOGICIAN NOTES:
            {logician_notes}

            OBJECTIVITY REVIEWER NOTES:
            {pov_notes}
            '''
            
            res3 = await client.aio.models.generate_content(
                model='gemini-2.5-flash',
                contents=agent_3_input,
                config=types.GenerateContentConfig(system_instruction=AGENT_3_PROMPT, temperature=0.2)
            )
            
            fixed_html = res3.text.strip()
            if fixed_html.startswith("```html"):
                fixed_html = fixed_html[7:]
            if fixed_html.startswith("```"):
                fixed_html = fixed_html[3:]
            if fixed_html.endswith("```"):
                fixed_html = fixed_html[:-3]
                
            return fixed_html.strip(), logician_notes, pov_notes
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"API Error: {e}, retrying in 45s...")
                await asyncio.sleep(45)
            else:
                raise e
    return "", "", ""

async def process_file(client: genai.Client, file_path: str, sem: asyncio.Semaphore):
    async with sem:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all <section> elements
        section_matches = list(re.finditer(r'(<section\b[^>]*>.*?</section>)', content, re.DOTALL))

        if not section_matches:
            return file_path, False, "No <section> elements found."

        all_logician_notes = []
        all_pov_notes = []

        new_content = content
        
        # Process from back to front to avoid index drift
        for idx, match in reversed(list(enumerate(section_matches))):
            original_html = match.group(1)
            
            try:
                fixed_html, n1, n2 = await process_element(client, original_html)
                
                # Prepend notes since we are iterating backward
                all_logician_notes.insert(0, f"### Section {idx+1}\n**Logician:**\n{n1}\n\n**POV Reviewer:**\n{n2}\n")
                
                # Replace content exactly where it was
                start, end = int(match.start(1)), int(match.end(1))
                new_content = new_content[:start] + fixed_html + new_content[end:]
                
                await asyncio.sleep(2)
            except Exception as e:
                return file_path, False, f"Error processing section {idx+1}: {str(e)}"

        # Write fixed content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        # Write notes to agy-npov-rvw.md in the respective directory
        dir_name = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)
        notes_path = os.path.join(dir_name, "agy-npov-rvw.md")
        
        with open(notes_path, 'a', encoding='utf-8') as f:
            f.write(f"\n## Review Notes for {base_name}\n\n")
            f.write("\n".join(all_logician_notes))
            f.write("\n---\n")

        print(f"[Done] {file_path}")
        return file_path, True, "Success"

async def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY is not set.")
        return

    client = genai.Client()
    
    # 1. Glob all *paper*.html
    base_dir = r"c:\Users\nafsa\src\read-rd"
    pattern = os.path.join(base_dir, "**", "*paper*.html")
    files = glob.glob(pattern, recursive=True)
    
    print(f"Found {len(files)} *paper*.html files to process.")
    
    # 2. Setup tracking file
    project_dir = os.path.join(base_dir, ".project")
    os.makedirs(project_dir, exist_ok=True)
    agents_file = os.path.join(project_dir, "agy-agents.md")
    
    if not os.path.exists(agents_file):
        with open(agents_file, 'w', encoding='utf-8') as f:
            f.write("# Agent Tracking for POV Review\n\n")
            f.write("## Agents Used\n")
            f.write("- **Agent 1 (Logician):** Evaluates logical consistency and scholastic rigor.\n")
            f.write("- **Agent 2 (Objectivity Reviewer):** Identifies personal POV and non-academic commentary.\n")
            f.write("- **Agent 3 (Academic Editor):** Rewrites content based on notes.\n\n")
            f.write("## File Processing Status\n\n")

    # 3. Process concurrently
    sem = asyncio.Semaphore(1)  # Limit concurrency to 1 to avoid 503s
    tasks = [process_file(client, f, sem) for f in files]
    
    for future in asyncio.as_completed(tasks):
        file_path, success, msg = await future
        
        # Log to agents file
        with open(agents_file, 'a', encoding='utf-8') as f:
            status = "✓" if success else "✗"
            f.write(f"- [{status}] `{file_path}`: {msg}\n")
            
        print(f"Status update: {file_path} -> {msg}")

if __name__ == "__main__":
    asyncio.run(main())
