import os
from PIL import Image

# Define output directory
OUTPUT_FILE = "./data/compressed_image.png"

def run_task(image_path: str, width: int = None, height: int = None, quality: int = 85):
    """Compresses and resizes an image, saving it to /data/compressed_image.png."""
    try:
        # Validate that image path is within /data/
        if not image_path.startswith("./data/"):
            return "❌ Access denied! Images must be inside /data/."

        # Check if the image file exists
        if not os.path.exists(image_path):
            return f"❌ Image file not found: {image_path}"

        # Open image
        img = Image.open(image_path)

        # Resize if dimensions provided
        if width and height:
            img = img.resize((width, height))

        # Save compressed image
        img.save(OUTPUT_FILE, format="PNG", quality=quality, optimize=True)

        return f"✅ Image compressed and saved as {OUTPUT_FILE}"

    except Exception as e:
        return f"❌ Error processing image: {e}"

# Debugging (if running this script directly)
if __name__ == "__main__":
    path = input("Enter image path (e.g., ./data/sample.png): ")
    print(run_task(path, width=500, height=500, quality=70))
