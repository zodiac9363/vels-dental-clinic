import os

def update_image_names():
    filepath = 'index.html'
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace("url('/assets/images/ortho_bg.png')", "url('/assets/images/ortho-hero.png')")
    content = content.replace("url('/assets/images/tooth_3d.png')", "url('/assets/images/tooth-hero.png')")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Updated image names in index.html")

if __name__ == "__main__":
    update_image_names()
