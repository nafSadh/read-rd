import os

repo_dir = r"c:\Users\nafsa\src\read-rd"

fixes = [
    ("cog-sci/religion-psychology/s1-csr.dd.html", "Cognitive Science of <em>Religion</em>", "<em>Cognitive</em> Science of Religion"),
    ("cog-sci/religion-psychology/s3-mental-health.dd.html", "Religion & Mental <em>Health</em>", "Religion & <em>Mental Health</em>"),
    ("cog-sci/religion-psychology/s4-morality.dd.html", "Moral Psychology & <em>Religion</em>", "<em>Moral</em> Psychology & Religion"),
    ("cog-sci/religion-psychology/s5-development.dd.html", "Developmental Psychology of <em>Religion</em>", "<em>Developmental</em> Psychology of Religion"),
    ("cog-sci/religion-psychology/s6-neuroscience.dd.html", "The Neuroscience of Religious <em>Experience</em>", "The <em>Neuroscience</em> of Religious Experience"),
    ("courses/scpd-ml/kv-cache.dd.html", "KV Cache in <em>LLM Inference</em>", "<em>KV Cache</em> in LLM Inference"),
    ("self/career.dd.html", "Career <em>Arc</em>", "<em>Career</em> Arc")
]

for rel_path, old_str, new_str in fixes:
    filepath = os.path.join(repo_dir, rel_path)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_str in content:
            new_content = content.replace(old_str, new_str)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {rel_path}")
        else:
            print(f"Could not find '{old_str}' in {rel_path}")
    else:
        print(f"File not found: {rel_path}")
