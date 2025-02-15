import os
import subprocess

markdown_file = "./data/format.md"

def run_task():
    """Formats the Markdown file /data/format.md using Prettier."""
    try:
        # Ensure Prettier is installed
        try:
            subprocess.run(["npx", "prettier", "--version"], check=True, capture_output=True, text=True)
        except FileNotFoundError:
            return "❌ Prettier is not installed. Please install using 'npm install -g prettier'."

        # Format the file using Prettier
        subprocess.run(["npx", "prettier", "--write", markdown_file], check=True)

        return f"✅ Markdown file formatted using Prettier."

    except subprocess.CalledProcessError as e:
        return f"❌ Error formatting markdown: {e}"

# Debugging (if running this script directly)
if __name__ == "__main__":
    print(run_task())
