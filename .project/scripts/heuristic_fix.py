import os
import glob
import re
import json

def main():
    repo_dir = r"c:\Users\nafsa\src\read-rd"
    pattern = os.path.join(repo_dir, "**", "*.dd.html")
    files = glob.glob(pattern, recursive=True)
    
    title_regex_sq = re.compile(r"(title:\s*')(.+?)(')")
    title_regex_dq = re.compile(r"(title:\s*\")(.+?)(\")")
    h1_regex = re.compile(r"(<h1[^>]*>)(.+?)(</h1>)")
    h2_regex = re.compile(r"(<h2[^>]*>)(.+?)(</h2>)")

    fixed_count = 0
    base_stopwords = {
        'the', 'a', 'an', 'and', 'or', 'of', 'to', 'in', 'for', 'with', 
        'on', 'at', 'by', 'from', 'as', 'vs', 'vs.', 'is', 'are', '&amp;', '&',
        'sources', 'references', 'overview', 'project', 'key', 'part', 'section',
        'what', 'where', 'why', 'how', 'does', 'do', 'can', 'could', 'should'
    }
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        # Determine subject stopwords based on parent directories
        folder_parts = filepath.replace('\\', '/').split('/')[-3:-1]
        local_stops = set(base_stopwords)
        for part in folder_parts:
            # e.g., "science-of-humor" -> ["science", "of", "humor"]
            words = part.replace('-', ' ').replace('_', ' ').split()
            for w in words:
                if len(w) > 2:
                    local_stops.add(w.lower())
                    # Also handle plural/singular roughly if ending in 's'
                    if w.endswith('s'):
                        local_stops.add(w[:-1].lower())
        
        def replacer(match):
            prefix = match.group(1)
            inner = match.group(2)
            suffix = match.group(3)
            
            # We ONLY want to modify titles that ALREADY HAVE an <em> tag
            # Because we assume the script is sweeping to FIX existing programmatic <em> tags.
            # If there's no <em>, we leave it alone.
            if '<em>' in inner:
                inner_clean = re.sub(r'</?em>', '', inner)
                
                # Split but keep whitespace and punctuation intact for exact reconstruction
                words = re.split(r'([A-Za-z0-9\-\u2019\']+)', inner_clean)
                for i, w in enumerate(words):
                    if re.match(r'^[A-Za-z0-9\-\u2019\']+$', w):
                        # It's a word. Check if it's a stopword.
                        if w.lower() not in local_stops:
                            # Found the differentiator!
                            words[i] = f"<em>{w}</em>"
                            break
                            
                new_inner = "".join(words)
                
                # If we somehow failed to find a non-stopword, fallback to first word
                if '<em>' not in new_inner:
                    for i, w in enumerate(words):
                        if re.match(r'^[A-Za-z0-9\-\u2019\']+$', w):
                            if w.lower() not in {'the', 'a', 'an', 'and', 'or', '&amp;'}:
                                words[i] = f"<em>{w}</em>"
                                break
                    new_inner = "".join(words)
                    
                return f"{prefix}{new_inner}{suffix}"
            return match.group(0)

        content = title_regex_sq.sub(replacer, content)
        content = title_regex_dq.sub(replacer, content)
        content = h1_regex.sub(replacer, content)
        content = h2_regex.sub(replacer, content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed_count += 1
            
    print(f"Applied heuristic accenting to {fixed_count} files.")

if __name__ == "__main__":
    main()
