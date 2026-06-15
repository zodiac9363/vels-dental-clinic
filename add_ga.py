import os
import glob
import re

GA_SNIPPET = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-ZKB7S3JN1B"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-ZKB7S3JN1B');
    </script>
"""

def add_ga_to_html():
    html_files = glob.glob("*.html") + glob.glob("services/*.html")
    for filepath in html_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        if "G-ZKB7S3JN1B" not in content:
            # Insert right after <head>
            content = content.replace("<head>", f"<head>\n{GA_SNIPPET}", 1)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added GA to {filepath}")
        else:
            print(f"GA already in {filepath}")

def add_ga_to_py():
    py_files = ["generate_services.py", "generate_legal.py"]
    for filepath in py_files:
        if not os.path.exists(filepath):
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "G-ZKB7S3JN1B" not in content:
            # Add to the head template. Both use a standard HTML template.
            content = content.replace("<head>", f"<head>\\n{GA_SNIPPET}", 1)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added GA to template in {filepath}")
        else:
            print(f"GA already in {filepath}")

if __name__ == "__main__":
    add_ga_to_html()
    add_ga_to_py()
