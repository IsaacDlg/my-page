
import re

def main():
    file_path = r'c:\Users\INTRO\OneDrive\Desktop\Mi CV\index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the IDs to replace
    ids_to_replace = ['SVGQp78JeTL', 'SVGTfP00bRe']
    
    # Find all occurrences of the python SVG block or just the IDs
    # Since the content is identical, we can split the content by the Python label or SVG start
    
    # Strategy: Find the second occurrence of the IDs and append a suffix
    
    new_content = content
    for svg_id in ids_to_replace:
        # Find all matches
        matches = [m.start() for m in re.finditer(svg_id, new_content)]
        
        # We expect at least 4 matches (2 definitions + 2 usages per SVG, times 2 SVGs? No)
        # The SVG code has:
        # <path fill="url(#ID)" ...>
        # <linearGradient id="ID" ...>
        # So each SVG has 2 occurrences of the ID.
        # Two SVGs means 4 occurrences total.
        # We want to change the 3rd and 4th occurrences (which belong to the second SVG).
        
        if len(matches) >= 4:
            # We need to replace the 3rd and 4th occurrences
            # It's safer to split the string and reconstruct it
            
            # Actually, let's just replace the second HALF of the file's occurrences?
            # Or better: find the "Duplicate List" comment and only replace after that.
            
            parts = new_content.split('<!-- Duplicate List for Infinite Loop -->')
            if len(parts) == 2:
                first_part = parts[0]
                second_part = parts[1]
                
                # Replace IDs in the second part
                second_part = second_part.replace(svg_id, svg_id + '_dup')
                
                new_content = first_part + '<!-- Duplicate List for Infinite Loop -->' + second_part
                print(f"Fixed duplicate ID: {svg_id}")
            else:
                print("Could not find Duplicate List comment")
        else:
            print(f"Not enough matches for ID {svg_id}: {len(matches)}")

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully fixed duplicate IDs")
    else:
        print("No changes made")

if __name__ == "__main__":
    main()
