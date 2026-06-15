import os

def fix_hero_tiles():
    filepath = 'index.html'
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the inline styles for hero-tile-2 and hero-tile-3
    content = content.replace(
        "style=\"background: url('/assets/images/ortho_bg.webp') center / cover no-repeat; align-items: flex-start;\"",
        "style=\"background-color: #E6F0FA; background-image: url('/assets/images/ortho_bg.png'); background-position: center; background-size: cover; background-repeat: no-repeat; align-items: flex-start;\""
    )
    
    content = content.replace(
        "style=\"background: url('/assets/images/tooth_3d.webp') center / cover no-repeat;\"",
        "style=\"background-color: #E6F0FA; background-image: url('/assets/images/tooth_3d.png'); background-position: center; background-size: cover; background-repeat: no-repeat;\""
    )
    
    # Also update the CSS version to bust cache
    content = content.replace('style.css?v=234567', 'style.css?v=999999')
    content = content.replace('style.css?v=111230', 'style.css?v=999999')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Fixed hero tiles in index.html")

if __name__ == "__main__":
    fix_hero_tiles()
