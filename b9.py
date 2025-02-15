import os
import markdown

# Define output file
OUTPUT_FILE = "./data/converted.html"

def run_task(md_path: str):
    """Converts a Markdown file to HTML and saves it to /data/converted.html."""
    try:
        # Validate that Markdown path is within /data/
        if not md_path.startswith("./data/"):
            return "❌ Access denied! Markdown files must be inside /data/."

        # Check if the Markdown file exists
        if not os.path.exists(md_path):
            return f"❌ Markdown file not found: {md_path}"

        # Read Markdown content
        with open(md_path, "r", encoding="utf-8") as file:
            md_content = file.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(md_content)

        # Save the converted HTML
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            file.write(html_content)

        return f"✅ Markdown converted to HTML and saved as {OUTPUT_FILE}"

    except Exception as e:
        return f"❌ Error converting Markdown: {e}"

# Debugging (if running this script directly)
if __name__ == "__main__":
    path = input("Enter Markdown file path (e.g., ./data/sample.md): ")
    print(run_task(path))
