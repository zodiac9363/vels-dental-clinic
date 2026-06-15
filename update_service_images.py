import os
import glob
import re

def update_images():
    # Update HTML files
    html_files = glob.glob('services/*.html')
    for file in html_files:
        if file == 'services/index.html':
            continue
            
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We want to replace something like:
        # <div style="background: url('/assets/images/cosmetic-dentistry.webp?v=2') center / cover no-repeat; border-radius: 16px; box-shadow: 0 12px 40px rgba(0,0,0,0.06); height: 350px;">
        # with:
        # <div class="service-hero-img" style="background-image: url('/assets/images/cosmetic-dentistry.webp?v=2');">
        
        # We can use regex to find this pattern
        pattern = r'<div style="background:\s*url\(\'(/assets/images/[^\']+)\'\)\s*center\s*/\s*cover\s*no-repeat;\s*border-radius:\s*16px;\s*box-shadow:[^;]+;\s*height:\s*350px;">'
        
        replacement = r'<div class="service-hero-img" style="background-image: url(\'\1\');">'
        
        new_content, count = re.subn(pattern, replacement, content)
        
        if count > 0:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
            
    # Update generate_services.py
    try:
        with open('generate_services.py', 'r', encoding='utf-8') as f:
            content = f.read()
            
        old_python_str = """<div style="background: url('/assets/images/{id}.webp?v=2') center / cover no-repeat; border-radius: 16px; box-shadow: 0 12px 40px rgba(0,0,0,0.06); height: 350px;">"""
        new_python_str = """<div class="service-hero-img" style="background-image: url('/assets/images/{id}.webp?v=2');">"""
        
        if old_python_str in content:
            content = content.replace(old_python_str, new_python_str)
            with open('generate_services.py', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Updated generate_services.py")
    except Exception as e:
        print("Error updating generate_services.py:", e)

if __name__ == "__main__":
    update_images()
