import os
import glob

def update_footer():
    html_files = glob.glob('*.html') + glob.glob('services/*.html')
    
    old_text = '<a href="tel:+918428828736" style="color: var(--mid-blue); display: block; margin-bottom: 20px;">8428828736</a>'
    new_text = '<a href="tel:+918428828736" style="color: var(--mid-blue); display: block; margin-bottom: 5px;">8428828736</a>\n                <a href="mailto:velsdentalclinictanjore@gmail.com" style="color: var(--mid-blue); display: block; margin-bottom: 20px; font-size: 0.85rem; word-break: break-all;">velsdentalclinictanjore@gmail.com</a>'
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if old_text in content:
            content = content.replace(old_text, new_text)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated footer in {file}")
        else:
            print(f"Text not found in {file}")
            
    # Also update generate_services.py
    with open('generate_services.py', 'r', encoding='utf-8') as f:
        content = f.read()
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open('generate_services.py', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated footer in generate_services.py")

if __name__ == "__main__":
    update_footer()
