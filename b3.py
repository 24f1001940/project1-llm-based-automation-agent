import os
import requests
import json

# Define output directory
DATA_DIR = "./data/"
OUTPUT_FILE = os.path.join(DATA_DIR, "api_response.json")

def run_task(api_url: str):
    """Fetches data from an API and saves it to /data/api_response.json."""
    try:
        if not api_url:
            return "❌ No API URL provided."

        # Ensure /data/ directory exists
        os.makedirs(DATA_DIR, exist_ok=True)

        # Fetch API response
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes

        # Save response JSON
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            json.dump(response.json(), file, indent=4)

        return f"✅ Data fetched from {api_url} and saved to {OUTPUT_FILE}"

    except requests.exceptions.RequestException as e:
        return f"❌ API request failed: {e}"

# Debugging (if running this script directly)
if __name__ == "__main__":
    print(run_task("https://jsonplaceholder.typicode.com/todos/1"))
