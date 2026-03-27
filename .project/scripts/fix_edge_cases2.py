import os
import glob
import re

def main():
    repo_dir = r"c:\Users\nafsa\src\read-rd"
    pattern = os.path.join(repo_dir, "**", "*.dd.html")
    files = glob.glob(pattern, recursive=True)
    
    fixed_count = 0
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        # Fix 1: &<em>amp</em>; Word -> &amp; <em>Word</em>
        # Also handles &<em>amp</em>; Mental Health -> &amp; <em>Mental</em> Health
        content = re.sub(r'&<em>amp</em>;\s*([A-Za-z0-9]+)', r'&amp; <em>\1</em>', content)
        
        # Edge case: Mental Health (both words might be capitalized, but above accents the first word, which is correct: <em>Mental</em> Health)
        
        # Fix 2: <em>word</em>.ext -> <em>word.ext</em>
        content = re.sub(r'<em>([A-Za-z0-9_\-]+)</em>(\.[A-Za-z0-9]+)', r'<em>\1\2</em>', content)
        
        # Fix 3: Other split HTML entities if any (like <em>lt</em>;) -> <em>&lt;</em> (none found but safe)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed_count += 1
            print(f"Fixed edge cases in: {os.path.relpath(filepath, repo_dir)}")
            
    print(f"Applied edge case fixes to {fixed_count} files.")

if __name__ == "__main__":
    main()
