import os
import glob
import re

favicon_tag = '    <link rel="icon" type="image/webp" href="/assets/images/logo.webp">\n    <link rel="apple-touch-icon" href="/assets/images/logo.webp">\n'

def add_favicon():
    html_files = glob.glob("*.html") + glob.glob("services/*.html") + ["generate_services.py", "generate_legal.py"]
    
    for filepath in html_files:
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if "rel=\"icon\"" in content:
            continue
            
        # Add after <meta name="viewport" ...>
        content = re.sub(
            r'(<meta name="viewport"[^>]*>)',
            r'\1\n' + favicon_tag,
            content
        )
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    print("Favicon added to all HTML files.")

if __name__ == "__main__":
    add_favicon()
