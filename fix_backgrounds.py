import os
import glob

def fix_css():
    html_files = glob.glob('*.html') + glob.glob('services/*.html') + ['generate_services.py', 'assets/css/style.css']
    
    for file in html_files:
        if not os.path.exists(file):
            continue
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace('center/cover', 'center / cover')
        new_content = new_content.replace('top/cover', 'top / cover')
        
        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed backgrounds in {file}")

if __name__ == "__main__":
    fix_css()
