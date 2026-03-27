import os
import glob
import json
import re

def extract_metadata(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        has_nb = 'NB_IMAGES' in content
        
        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        title = title_match.group(1) if title_match else ""
        
        # Extract hero-title
        hero_match = re.search(r'<div class="hero-title">(.*?)</div>', content, re.IGNORECASE)
        hero = hero_match.group(1) if hero_match else ""
        hero = re.sub(r'<[^>]+>', '', hero) # strip tags
        
        # Extract masthead-sub
        sub_match = re.search(r'<div class="masthead-sub">.*?<span>(.*?)</span>.*?</div>', content, re.IGNORECASE | re.DOTALL)
        if not sub_match:
            sub_match = re.search(r'<div class="masthead-sub">(.*?)</div>', content, re.IGNORECASE | re.DOTALL)
        sub = sub_match.group(1) if sub_match else ""
        sub = re.sub(r'<[^>]+>', '', sub).strip()
        
        return {
            'file': filepath,
            'title': title,
            'hero': hero,
            'sub': sub,
            'has_nb': has_nb
        }
    except Exception as e:
        return {'file': filepath, 'error': str(e)}

def main():
    search_dir = r"c:\Users\nafsa\src\read-rd"
    files = []
    for root, _, filenames in os.walk(search_dir):
        if 'node_modules' in root or '.git' in root:
            continue
        for filename in filenames:
            if filename.endswith('.dd.html') or filename.endswith('.sd.html'):
                files.append(os.path.join(root, filename))
                
    results = []
    for f in files:
        results.append(extract_metadata(f))
        
    with open(r"c:\Users\nafsa\src\read-rd\tmp_meta.json", "w", encoding='utf-8') as f:
        json.dump(results, f, indent=2)
        
    print(f"Extracted metadata for {len(files)} files.")

if __name__ == '__main__':
    main()
