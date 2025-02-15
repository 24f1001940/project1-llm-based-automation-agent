# import os
# import openai
# import pytesseract
# from PIL import Image

# # Get AI Proxy Token
# AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
# if not AIPROXY_TOKEN:
#     raise ValueError("AIPROXY_TOKEN is not set! Please log in to AI Proxy.")

# AIPROXY_TOKEN = AIPROXY_TOKEN.strip()

# print(f"AIPROXY_TOKEN: {repr(AIPROXY_TOKEN)}")  

# # Configure OpenAI API with AI Proxy
# client = openai.OpenAI(api_key=AIPROXY_TOKEN, base_url="https://aiproxy.sanand.workers.dev/openai/v1/")

# # Define file paths
# image_file = "./data/credit_card.png"
# output_file = "./data/credit-card.txt"

# # Read image and extract text using Tesseract OCR
# try:
#     image = Image.open(image_file)
#     extracted_text = pytesseract.image_to_string(image)
#     print(f"OCR Extracted Text: {extracted_text.strip()}")
# except Exception as e:
#     raise ValueError(f"Error in OCR processing: {e}")

# # Use LLM to extract only the credit card number
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "Extract and return only the credit card number without spaces."},
#         {"role": "user", "content": extracted_text}
#     ]
# )

# # Extract cleaned credit card number
# credit_card_number = response.choices[0].message.content.strip().replace(" ", "")

# # Save extracted credit card number to a file
# with open(output_file, "w", encoding="utf-8") as file:
#     file.write(credit_card_number)

# print(f"✅ Extracted credit card number saved to {output_file}: {credit_card_number}")

import os
import openai
import pytesseract
from PIL import Image

AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN", "").strip()
if not AIPROXY_TOKEN:
    raise ValueError("AIPROXY_TOKEN is not set! Please log in to AI Proxy.")

client = openai.OpenAI(api_key=AIPROXY_TOKEN, base_url="https://aiproxy.sanand.workers.dev/openai/v1/")
image_file = "./data/credit_card.png"
output_file = "./data/credit-card.txt"

def run_task():
    """Extracts a credit card number from an image using OCR and LLM."""
    try:
        image = Image.open(image_file)
        extracted_text = pytesseract.image_to_string(image).strip()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Extract only the credit card number: {extracted_text}"}]
        )

        credit_card_number = response.choices[0].message.content.strip().replace(" ", "")
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(credit_card_number)

        return f"✅ Extracted credit card number saved to {output_file}: {credit_card_number}"

    except Exception as e:
        return f"❌ Error processing credit card extraction: {e}"
