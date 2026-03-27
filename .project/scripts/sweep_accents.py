import os
import glob
import json
import re

def main():
    repo_dir = r"c:\Users\nafsa\src\read-rd"
    pattern = os.path.join(repo_dir, "**", "*.dd.html")
    files = glob.glob(pattern, recursive=True)
    
    report = {}
    
    title_pattern = re.compile(r"title:\s*['\"](.*?)['\"]", re.IGNORECASE)
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        matches = title_pattern.findall(content)
        headers = []
        for match in matches:
            if '<em>' in match:
                headers.append(match)
                
        if headers:
            rel_path = os.path.relpath(filepath, repo_dir).replace('\\', '/')
            report[rel_path] = headers
            
    out_path = os.path.join(repo_dir, "accents_js_report.json")
    with open(out_path, "w", encoding="utf-8") as out:
        json.dump(report, out, indent=2)
        
    print(f"Report generated at {out_path} with {len(report)} files.")

if __name__ == "__main__":
    main()
