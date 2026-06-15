import os
import re
from PIL import Image
import glob

IMAGE_DIR = "assets/images"
HTML_DIRS = [".", "services"]
PY_FILES = ["generate_services.py"]

def convert_images_to_webp():
    print("Converting images to WEBP...")
    for ext in ("*.png", "*.jpg", "*.jpeg"):
        for filepath in glob.glob(os.path.join(IMAGE_DIR, ext)):
            filename = os.path.basename(filepath)
            name, _ = os.path.splitext(filename)
            webp_path = os.path.join(IMAGE_DIR, f"{name}.webp")
            
            if not os.path.exists(webp_path):
                try:
                    with Image.open(filepath) as img:
                        img.convert("RGB").save(webp_path, "WEBP", quality=85)
                    print(f"Converted {filename} -> {name}.webp")
                except Exception as e:
                    print(f"Error converting {filename}: {e}")

def optimize_html_files():
    print("Optimizing HTML and PY files...")
    
    # Process HTML files
    for d in HTML_DIRS:
        for filepath in glob.glob(os.path.join(d, "*.html")):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Replace extensions
            content = re.sub(r'\.png\b', '.webp', content)
            content = re.sub(r'\.jpg\b', '.webp', content)
            content = re.sub(r'\.jpeg\b', '.webp', content)

            # Add loading="lazy" to all imgs except those with 'logo'
            def add_lazy(match):
                img_tag = match.group(0)
                if 'loading="lazy"' in img_tag:
                    return img_tag
                if 'logo.webp' in img_tag or 'logo.jpeg' in img_tag:
                    return img_tag # Don't lazy load logo
                
                return img_tag.replace('<img ', '<img loading="lazy" ')

            content = re.sub(r'<img\s+[^>]+>', add_lazy, content)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Optimized {filepath}")
            
    # Process PY files
    for filepath in PY_FILES:
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            content = re.sub(r'\.png\b', '.webp', content)
            content = re.sub(r'\.jpg\b', '.webp', content)
            content = re.sub(r'\.jpeg\b', '.webp', content)
            
            # Update generate_services.py HTML template
            def add_lazy(match):
                img_tag = match.group(0)
                if 'loading="lazy"' in img_tag:
                    return img_tag
                if 'logo.webp' in img_tag or 'logo.jpeg' in img_tag:
                    return img_tag
                return img_tag.replace('<img ', '<img loading="lazy" ')
            
            content = re.sub(r'<img\s+[^>]+>', add_lazy, content)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Optimized {filepath}")

if __name__ == "__main__":
    convert_images_to_webp()
    optimize_html_files()
    print("Done!")
