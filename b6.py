import os
import json
import requests
from bs4 import BeautifulSoup

# Define output file
OUTPUT_FILE = "./data/web_scraped_data.json"
ALLOWED_DOMAINS = ["jsonplaceholder.typicode.com", "example.com"]  # Add more if needed

def run_task(url: str, selector: str = None):
    """Scrapes a website and saves the extracted data to a JSON file."""
    try:
        # Validate URL
        domain = url.split("/")[2]
        if domain not in ALLOWED_DOMAINS:
            return f"❌ Access to domain '{domain}' is not allowed."

        # Fetch the webpage content
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse the webpage content
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract content based on selector
        if selector:
            elements = soup.select(selector)
            data = [el.get_text(strip=True) for el in elements]
        else:
            # Extract all text if no selector provided
            data = soup.get_text(strip=True)

        # Save results to JSON
        result = {"url": url, "content": data}
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)

       
