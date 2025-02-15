import os
import subprocess

datagen_script = "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py"
output_dir = "./data/"

def run_task():
    """Installs 'uv' (if required) and runs datagen.py with a user email."""
    try:
        # Ensure 'uv' is installed
        try:
            subprocess.run(["uv", "--version"], check=True, capture_output=True, text=True)
        except FileNotFoundError:
            print("🔹 'uv' not found. Installing...")
            subprocess.run(["pip", "install", "uv"], check=True)

        # Run datagen.py
        user_email = os.getenv("USER_EMAIL", "user@example.com")  # Use an env variable or default email
        subprocess.run(["python", "-m", "urllib.request", datagen_script, user_email], check=True)

        return f"✅ 'uv' installed and datagen.py executed with {user_email}."

    except subprocess.CalledProcessError as e:
        return f"❌ Error executing command: {e}"

# Debugging (if running this script directly)
if __name__ == "__main__":
    print(run_task())
