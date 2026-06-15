import os
import glob

def add_tech_link():
    files = glob.glob('**/*.html', recursive=True)
    files.extend(['generate_services.py', 'generate_legal.py'])
    
    for file in files:
        if not os.path.exists(file): continue
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '<li><a href="/index.html#reviews">Reviews</a></li>' in content and 'Technology' not in content:
            new_content = content.replace(
                '<li><a href="/index.html#reviews">Reviews</a></li>',
                '<li><a href="/technology.html">Technology & Equipment</a></li>\n                    <li><a href="/index.html#reviews">Reviews</a></li>'
            )
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
                print(f"Updated {file}")

add_tech_link()