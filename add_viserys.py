import os
import glob

def add_viserys_credits():
    html_files = glob.glob('*.html') + glob.glob('services/*.html')
    
    old_text = '        </div>\n        <div class="giant-wordmark">VELS DENTAL</div>'
    new_text = '        </div>\n        <div class="footer-credits">\n            Designed &amp; Developed by <a href="https://viserys.netlify.app/" target="_blank" rel="noopener noreferrer">VISERYS</a>\n        </div>\n        <div class="giant-wordmark">VELS DENTAL</div>'
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if old_text in content and "Designed &amp; Developed by" not in content:
            content = content.replace(old_text, new_text)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added credits to {file}")
        else:
            print(f"Skipped {file} (already added or target string not found)")
            
    # Update generate_services.py as well so future generated files have it
    try:
        with open('generate_services.py', 'r', encoding='utf-8') as f:
            content = f.read()
        if old_text in content and "Designed &amp; Developed by" not in content:
            content = content.replace(old_text, new_text)
            with open('generate_services.py', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Added credits to generate_services.py")
    except Exception as e:
        print("generate_services.py error:", e)

if __name__ == "__main__":
    add_viserys_credits()
