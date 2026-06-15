import shutil
from PIL import Image
import os

source_path = r"C:\Users\heavi\.gemini\antigravity-ide\brain\74933533-2880-4799-9a99-3ebab8dd5bf5\digital_dentistry_hero_1781506038452.png"
dest_dir = r"z:\VELS dental\assets\images"
dest_webp = os.path.join(dest_dir, "digital-dentistry.webp")
dest_png = os.path.join(dest_dir, "digital-dentistry.png")

# Copy the original PNG
shutil.copy(source_path, dest_png)

# Convert and save as WEBP
try:
    with Image.open(source_path) as img:
        img.convert("RGB").save(dest_webp, "WEBP", quality=85)
    print(f"Successfully converted and saved to {dest_webp}")
except Exception as e:
    print(f"Error: {e}")
