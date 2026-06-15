import os
import glob
import re

def fix_lighthouse_issues():
    html_files = glob.glob("*.html") + glob.glob("services/*.html") + ["generate_services.py", "generate_legal.py"]
    
    for filepath in html_files:
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. ARIA Labels for Buttons
        content = re.sub(r'<button class="hamburger"[^>]*>', r'<button class="hamburger" aria-label="Toggle Menu">', content)
        content = re.sub(r'<button class="mobile-menu-close"[^>]*>', r'<button class="mobile-menu-close" aria-label="Close Menu">', content)
        content = re.sub(r'<button class="back-top"[^>]*>', r'<button class="back-top" aria-label="Back to Top">', content)
        
        # 2. ARIA Labels for links
        content = re.sub(r'(<a[^>]*class="wa-fab"[^>]*)>', r'\1 aria-label="Chat on WhatsApp">', content)
        
        # 3. Form elements ARIA labels
        content = re.sub(r'(<input type="text" id="pat-name"[^>]*)>', r'\1 aria-label="Your full name">', content)
        content = re.sub(r'(<input type="tel" id="pat-phone"[^>]*)>', r'\1 aria-label="Your WhatsApp number">', content)
        content = re.sub(r'(<input type="date" id="pref-date"[^>]*)>', r'\1 aria-label="Preferred Date">', content)
        content = re.sub(r'(<select id="pref-doc"[^>]*)>', r'\1 aria-label="Preferred Doctor">', content)
        content = re.sub(r'(<select id="pref-treat"[^>]*)>', r'\1 aria-label="Preferred Treatment">', content)
        content = re.sub(r'(<input type="checkbox"[^>]*)(>)', lambda m: f'{m.group(1)} aria-label="Accept Privacy Policy"{m.group(2)}' if 'aria-label' not in m.group(1) else m.group(0), content)
        
        # 4. Logo explicit width and height
        content = re.sub(r'(<img src="/assets/images/logo\.(webp|jpeg|png|jpg)" alt="Vels Dental Clinic Logo")([^>]*)>', r'\1 width="116" height="72"\3>', content)

        # Remove duplicate aria-labels just in case
        content = re.sub(r'aria-label="[^"]*"\s+aria-label="[^"]*"', 'aria-label="Fixed Label"', content)
        
        # 5. Fix Heading Sequential Order in generate_services.py
        if filepath == "generate_services.py":
            content = content.replace('<h3 class="inter" style="font-size: 2rem; font-weight: 700; margin-bottom: 16px;">What is', '<h2 class="inter" style="font-size: 2rem; font-weight: 700; margin-bottom: 16px;">What is')
            content = content.replace('<h3 class="inter" style="font-size: 2rem; font-weight: 700; text-align: center; margin-bottom: 40px;">Types We Offer</h3>', '<h2 class="inter" style="font-size: 2rem; font-weight: 700; text-align: center; margin-bottom: 40px;">Types We Offer</h2>')
            content = content.replace('<h3 class="inter" style="font-size: 2rem; font-weight: 700; text-align: center; margin-bottom: 40px;">Treatment Process</h3>', '<h2 class="inter" style="font-size: 2rem; font-weight: 700; text-align: center; margin-bottom: 40px;">Treatment Process</h2>')
            content = content.replace('<h3 class="inter" style="font-size: 2rem; font-weight: 700; text-align: center; margin-bottom: 40px;">Key Benefits</h3>', '<h2 class="inter" style="font-size: 2rem; font-weight: 700; text-align: center; margin-bottom: 40px;">Key Benefits</h2>')
            content = content.replace('<h3 class="inter" style="font-size: 2rem; font-weight: 700; margin-bottom: 40px;">Frequently Asked Questions</h3>', '<h2 class="inter" style="font-size: 2rem; font-weight: 700; margin-bottom: 40px;">Frequently Asked Questions</h2>')
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    print("Lighthouse issues fixed across all HTML files.")

if __name__ == "__main__":
    fix_lighthouse_issues()
