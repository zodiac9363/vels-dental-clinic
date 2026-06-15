import os
import glob

def update_email():
    html_files = glob.glob('*.html') + glob.glob('services/*.html') + ['generate_services.py', 'update_footer.py']
    
    for file in html_files:
        if not os.path.exists(file):
            continue
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace('velsdentalclinicthanjavur@gmail.com', 'velsdentalclinictanjore@gmail.com')
        
        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated email in {file}")

if __name__ == "__main__":
    update_email()
