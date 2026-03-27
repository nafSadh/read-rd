import subprocess

def main():
    repo_dir = r"c:\Users\nafsa\src\read-rd"
    try:
        out = subprocess.check_output(['git', 'diff', '--unified=0'], cwd=repo_dir, text=True, encoding='utf-8')
    except Exception as e:
        print("Error running git diff", e)
        return

    changes = []
    current_file = ""
    old_val = None

    for line in out.splitlines():
        if line.startswith('+++ b/'):
            current_file = line[6:]
        elif line.startswith('-') and not line.startswith('---'):
            if 'title:' in line or '<h1' in line or '<h2' in line:
                old_val = line[1:].strip()
        elif line.startswith('+') and not line.startswith('+++'):
            if 'title:' in line or '<h1' in line or '<h2' in line:
                new_val = line[1:].strip()
                if old_val:
                    # try to extract just the title string to make it readable
                    changes.append(f"**{current_file}**\nold: `{old_val}`\nnew: `{new_val}`\n")
                    old_val = None

    with open(os.path.join(repo_dir, "title_changes_review.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(changes))
        
    print(f"Generated review document with {len(changes)} changes.")

import os
if __name__ == "__main__":
    main()
