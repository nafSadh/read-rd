import re
import os

def main():
    repo_dir = r"c:\Users\nafsa\src\read-rd"
    filepath = os.path.join(repo_dir, "title_changes_review.md")
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    edge_cases = []
    
    # regex to find single letters, URL chunks, or HTML entities
    # we look for lines starting with "new: "
    for line in content.splitlines():
        if line.startswith("new:"):
            # find the <em>...</em> 
            em_match = re.search(r'<em>(.*?)</em>', line)
            if em_match:
                inner = em_match.group(1)
                
                # if it's "amp" or "lt" or similar, or 1-2 letters, or followed strictly by dots
                if inner in ['amp', 'lt', 'gt', 'quot', 'apos'] or len(inner) <= 2 or '.' in line or '&' in line:
                    edge_cases.append(line)
                    
    with open(os.path.join(repo_dir, "edge_cases.md"), "w", encoding="utf-8") as out:
        out.write("\n".join(edge_cases))
        
    print(f"Found {len(edge_cases)} potential edge cases.")

if __name__ == "__main__":
    main()
