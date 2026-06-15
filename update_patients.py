import os
import glob

def update_patients():
    html_files = glob.glob('*.html') + glob.glob('services/*.html')
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace('5000+', '15000+')
        new_content = new_content.replace('5,000+', '15,000+')
        
        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated patients in {file}")

if __name__ == "__main__":
    update_patients()
