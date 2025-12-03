
def main():
    file_path = r'c:\Users\INTRO\OneDrive\Desktop\Mi CV\StyleCSS.css'
    search_terms = ['marquee', 'skills']
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for i, line in enumerate(lines):
            for term in search_terms:
                if term in line:
                    print(f"Found '{term}' on line {i+1}: {line.strip()}")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    main()
