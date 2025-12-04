
import os
import re

file_path = r'c:\Users\INTRO\OneDrive\Desktop\Mi CV\StyleCSS.css'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Regex to find the .profile-avatar block and its background property
# We look for .profile-avatar { ... } and capture the content
# Then we replace the background line.

pattern = r'(\.profile-avatar\s*\{[^}]*background:\s*)([^;]+)(;[^}]*\})'

# We want to replace the captured background value with #1e3a8a
# Group 1 is ".profile-avatar { ... background: "
# Group 2 is the current value (e.g. "var(--accent)" or "conic-gradient(...)")
# Group 3 is "; ... }"

if re.search(pattern, content, re.DOTALL):
    new_content = re.sub(pattern, r'\1#1e3a8a\3', content, flags=re.DOTALL)
    
    # Also check if it's already correct to avoid unnecessary writes (though harmless)
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully updated profile avatar background to #1e3a8a.")
    else:
        print("Profile avatar background is already #1e3a8a.")
else:
    print("Could not find .profile-avatar block.")
