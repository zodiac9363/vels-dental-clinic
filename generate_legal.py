import os
import re

# Read template structure from generate_services.py
with open("generate_services.py", "r", encoding="utf-8") as f:
    content = f.read()

# Extract header (up to </nav>)
header_match = re.search(r'HTML_TEMPLATE = """(.*?</nav>)', content, re.DOTALL)
header = header_match.group(1) if header_match else ""

# The meta tags in the header have {name} and {description} placeholders from the services generator
# We need to replace them with generic ones for the legal pages
header = header.replace("<title>{name} in Thanjavur | Vels Dental Clinic</title>", "<title>{name} | Vels Dental Clinic</title>")
header = header.replace('content="{name} in Thanjavur | Vels Dental Clinic"', 'content="{name} | Vels Dental Clinic"')
header = header.replace('content="{description}"', 'content="Read our {name} at Vels Dental Clinic."')
header = header.replace('href="https://velsdental.in/services/{id}.html"', 'href="https://velsdental.in/{id}.html"')

# Extract footer (from <!-- Footer --> to the end)
footer_match = re.search(r'(<!-- Footer -->.*?)"""', content, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""

privacy_content = f"""{header}
    <div class="mobile-menu-overlay">
        <button class="mobile-menu-close" aria-label="Close Menu"><i class="fas fa-times"></i></button>
        <a href="/">Home</a><a href="/about.html">About</a><a href="/doctors.html">Our Doctors</a>
        <a href="/services/index.html">Services</a><a href="/contact.html">Contact</a>
        <a href="/appointment.html" class="btn btn-primary" style="color:var(--white);">Book Appointment</a>
    </div>

    <main>
        <div class="breadcrumb-wrap">
            <div class="container breadcrumb">
                <ol><li><a href="/">Home</a></li><li>Privacy Policy</li></ol>
            </div>
        </div>

        <section class="section-pad bg-white">
            <div class="container" style="max-width: 800px; margin: 0 auto;">
                <h1 class="inter" style="font-size: clamp(2rem, 4vw, 2.5rem); font-weight: 700; margin-bottom: 24px;">Privacy Policy</h1>
                <p class="inter" style="color: var(--muted); margin-bottom: 24px;"><strong>Effective Date:</strong> January 1, 2025</p>
                
                <div class="inter" style="line-height: 1.7; color: var(--text);">
                    <p style="margin-bottom: 16px;">Welcome to Vels Dental Clinic. We are committed to protecting your personal information and your right to privacy. This Privacy Policy explains how we collect, use, and safeguard your information when you visit our clinic or use our website.</p>
                    
                    <h2 style="font-size: 1.2rem; font-weight: 600; margin-top: 32px; margin-bottom: 12px;">1. Information We Collect</h2>
                    <p style="margin-bottom: 16px;">We may collect personal information that you voluntarily provide to us when booking an appointment or contacting us, including:</p>
                    <ul style="margin-bottom: 16px; padding-left: 20px;">
                        <li style="margin-bottom: 8px;">Name, Phone Number, and Email Address.</li>
                        <li style="margin-bottom: 8px;">Medical history and dental records relevant to your treatment.</li>
                        <li style="margin-bottom: 8px;">Any other information you choose to provide via WhatsApp or phone.</li>
                    </ul>

                    <h2 style="font-size: 1.2rem; font-weight: 600; margin-top: 32px; margin-bottom: 12px;">2. How We Use Your Information</h2>
                    <p style="margin-bottom: 16px;">The information we collect is used strictly for:</p>
                    <ul style="margin-bottom: 16px; padding-left: 20px;">
                        <li style="margin-bottom: 8px;">Scheduling and managing your dental appointments.</li>
                        <li style="margin-bottom: 8px;">Providing personalized dental care and maintaining accurate patient records.</li>
                        <li style="margin-bottom: 8px;">Communicating with you regarding appointment reminders or follow-up care.</li>
                    </ul>

                    <h2 style="font-size: 1.2rem; font-weight: 600; margin-top: 32px; margin-bottom: 12px;">3. Data Security</h2>
                    <p style="margin-bottom: 16px;">We implement appropriate technical and organizational security measures designed to protect the security of any personal information we process. Your medical records are kept strictly confidential.</p>

                    <h2 style="font-size: 1.2rem; font-weight: 600; margin-top: 32px; margin-bottom: 12px;">4. Sharing Your Information</h2>
                    <p style="margin-bottom: 16px;">We do not sell, trade, or rent your personal identification information to others. We will only share your information with third parties when legally required or with specialist doctors referred with your explicit consent.</p>

                    <h2 style="font-size: 1.2rem; font-weight: 600; margin-top: 32px; margin-bottom: 12px;">5. Contact Us</h2>
                    <p style="margin-bottom: 16px;">If you have questions or comments about this notice, you may email us or contact us at:</p>
                    <p style="margin-bottom: 16px;"><strong>Vels Dental Clinic</strong><br>Anna Nagar Bus Stop, Nanjikottai Road<br>Thanjavur, Tamil Nadu 613006<br>Phone: 9894888736</p>
                </div>
            </div>
        </section>
    </main>
{footer}"""

terms_content = f"""{header}
    <div class="mobile-menu-overlay">
        <button class="mobile-menu-close" aria-label="Close Menu"><i class="fas fa-times"></i></button>
        <a href="/">Home</a><a href="/about.html">About</a><a href="/doctors.html">Our Doctors</a>
        <a href="/services/index.html">Services</a><a href="/contact.html">Contact</a>
        <a href="/appointment.html" class="btn btn-primary" style="color:var(--white);">Book Appointment</a>
    </div>

    <main>
        <div class="breadcrumb-wrap">
            <div class="container breadcrumb">
                <ol><li><a href="/">Home</a></li><li>Terms & Conditions</li></ol>
            </div>
        </div>

        <section class="section-pad bg-white">
            <div class="container" style="max-width: 800px; margin: 0 auto;">
                <h1 class="inter" style="font-size: clamp(2rem, 4vw, 2.5rem); font-weight: 700; margin-bottom: 24px;">Terms & Conditions</h1>
                <p class="inter" style="color: var(--muted); margin-bottom: 24px;"><strong>Effective Date:</strong> January 1, 2025</p>
                
                <div class="inter" style="line-height: 1.7; color: var(--text);">
                    <p style="margin-bottom: 16px;">By accessing and using the Vels Dental Clinic website, you agree to be bound by the following terms and conditions. If you do not agree to these terms, please do not use our website.</p>
                    
                    <h2 style="font-size: 1.2rem; font-weight: 600; margin-top: 32px; margin-bottom: 12px;">1. Medical Disclaimer</h2>
                    <p style="margin-bottom: 16px;">The content provided on this website is for informational purposes only and is not a substitute for professional medical or dental advice, diagnosis, or treatment. Always seek the advice of your dentist or other qualified health provider with any questions you may have regarding a dental condition.</p>

                    <h2 style="font-size: 1.2rem; font-weight: 600; margin-top: 32px; margin-bottom: 12px;">2. Appointments & Cancellations</h2>
                    <p style="margin-bottom: 16px;">When you book an appointment via our website or WhatsApp, your time slot is reserved exclusively for you. We kindly request at least 24 hours' notice if you need to cancel or reschedule your appointment so that we may offer the time to another patient.</p>

                    <h2 style="font-size: 1.2rem; font-weight: 600; margin-top: 32px; margin-bottom: 12px;">3. Intellectual Property</h2>
                    <p style="margin-bottom: 16px;">All content on this website, including text, graphics, logos, and images, is the property of Vels Dental Clinic and is protected by intellectual property laws. You may not reproduce, distribute, or create derivative works from this content without our express written permission.</p>

                    <h2 style="font-size: 1.2rem; font-weight: 600; margin-top: 32px; margin-bottom: 12px;">4. Limitation of Liability</h2>
                    <p style="margin-bottom: 16px;">Vels Dental Clinic shall not be liable for any direct, indirect, incidental, or consequential damages arising out of your use or inability to use this website or the information contained herein.</p>

                    <h2 style="font-size: 1.2rem; font-weight: 600; margin-top: 32px; margin-bottom: 12px;">5. Changes to Terms</h2>
                    <p style="margin-bottom: 16px;">We reserve the right to modify these terms at any time. Any changes will be posted on this page, and your continued use of the website constitutes your acceptance of the revised terms.</p>
                </div>
            </div>
        </section>
    </main>
{footer}"""

with open("privacy-policy.html", "w", encoding="utf-8") as f:
    f.write(privacy_content.replace("{name}", "Privacy Policy").replace("{id}", "privacy-policy"))

with open("terms-conditions.html", "w", encoding="utf-8") as f:
    f.write(terms_content.replace("{name}", "Terms & Conditions").replace("{id}", "terms-conditions"))

print("Created privacy-policy.html and terms-conditions.html")
