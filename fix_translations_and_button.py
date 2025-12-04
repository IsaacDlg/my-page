
import re
import os

def main():
    # 1. Update HTML (Add data-i18n attributes)
    html_path = r'c:\Users\INTRO\OneDrive\Desktop\Mi CV\index.html'
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Replace "Producción" with data-i18n
        # Target: </svg> Producción</span>
        if 'data-i18n="metric_production"' not in html_content:
            html_content = html_content.replace('</svg> Producción</span>', '</svg> <span data-i18n="metric_production">Producción</span></span>')
            print("Added data-i18n to Producción")
        
        # Replace "Código abierto" with data-i18n
        # Target: </svg> Código abierto</strong>
        if 'data-i18n="metric_opensource"' not in html_content:
            html_content = html_content.replace('</svg> Código abierto</strong>', '</svg> <span data-i18n="metric_opensource">Código abierto</span></strong>')
            print("Added data-i18n to Código abierto")
            
        # Replace "Ver GitHub" button text with data-i18n
        # Target: Ver GitHub
        # This is risky as "Ver GitHub" might appear elsewhere or be part of a larger string.
        # But looking at the file, it's inside an <a> tag.
        # <a href="https://github.com/IsaacDlg" ...>
        #     Ver GitHub
        # </a>
        # Let's use regex to be safer.
        # Match the button specifically
        btn_regex = re.compile(r'(<a href="https://github\.com/IsaacDlg"[^>]*>\s*)Ver GitHub(\s*</a>)')
        if btn_regex.search(html_content):
            html_content = btn_regex.sub(r'\1<span data-i18n="btn_github">Ver GitHub</span>\2', html_content)
            print("Added data-i18n to Ver GitHub button")

        # Update translations object
        # We need to find `const translations = {` and insert our new keys.
        # Or just replace the whole object if we had it all, but we don't want to carry that payload.
        # Better to insert into the existing JSON string.
        # It looks like: const translations = {"nav_projects": ...
        # We can just replace `const translations = {` with `const translations = {"metric_production": {"es": "Producción", "en": "Production"}, "metric_opensource": {"es": "Código abierto", "en": "Open Source"}, "btn_github": {"es": "Ver GitHub", "en": "View GitHub"}, `
        
        if '"metric_production":' not in html_content:
            html_content = html_content.replace('const translations = {', 'const translations = {"metric_production": {"es": "Producción", "en": "Production"}, "metric_opensource": {"es": "Código abierto", "en": "Open Source"}, "btn_github": {"es": "Ver GitHub", "en": "View GitHub"}, ')
            print("Updated translations object")

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("Successfully updated index.html")

    except Exception as e:
        print(f"Error updating HTML: {e}")

    # 2. Update CSS (Fix button alignment)
    css_path = r'c:\Users\INTRO\OneDrive\Desktop\Mi CV\StyleCSS.css'
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
            
        # We want to add justify-content: center to .hero-github a
        # Current block:
        # .hero-github a {
        #     font-size: 0.76rem;
        #     padding: 0.25rem 0.65rem;
        #     border-radius: 999px;
        #     background: rgba(15, 23, 42, 1);
        #     border: 1px solid rgba(55, 65, 81, 0.9);
        # }
        
        # We can append the fix or replace the block. Appending a specific rule is safer.
        css_append = """
/* Fix GitHub button alignment */
.hero-github a {
    display: inline-flex;
    align-items: center;
    justify-content: center;
}
"""
        if '/* Fix GitHub button alignment */' not in css_content:
            with open(css_path, 'a', encoding='utf-8') as f:
                f.write(css_append)
            print("Successfully updated StyleCSS.css")
        else:
            print("CSS fix already present")

    except Exception as e:
        print(f"Error updating CSS: {e}")

if __name__ == "__main__":
    main()
