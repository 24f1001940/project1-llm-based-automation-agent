# import os
# import openai

# # Get AI Proxy Token
# AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
# if not AIPROXY_TOKEN:
#     raise ValueError("AIPROXY_TOKEN is not set! Please log in to AI Proxy.")

# AIPROXY_TOKEN = AIPROXY_TOKEN.strip()
# print(f"AIPROXY_TOKEN: {AIPROXY_TOKEN}") 

# # Configure OpenAI API with AI Proxy
# client = openai.OpenAI(api_key=AIPROXY_TOKEN, base_url="https://aiproxy.sanand.workers.dev/openai/v1/")

# # Define file paths
# email_file = "./data/email.txt"
# output_file = "./data/email-sender.txt"

# # Read email content
# with open(email_file, "r", encoding="utf-8") as file:
#     email_content = file.read()

# # Use LLM to extract sender's email
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "Extract the sender's email from this email message."},
#         {"role": "user", "content": email_content}
#     ]
# )

# # Extract email address from response
# extracted_email = response.choices[0].message.content.strip()

# # Save extracted email to a file
# with open(output_file, "w", encoding="utf-8") as file:
#     file.write(extracted_email)

# print(f"✅ Extracted email saved to {output_file}: {extracted_email}")

import os
import openai

AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN", "").strip()
if not AIPROXY_TOKEN:
    raise ValueError("AIPROXY_TOKEN is not set! Please log in to AI Proxy.")

client = openai.OpenAI(api_key=AIPROXY_TOKEN, base_url="https://aiproxy.sanand.workers.dev/openai/v1/")
email_file = "./data/email.txt"
output_file = "./data/email-sender.txt"

def run_task():
    """Extracts the sender's email address from an email message."""
    try:
        with open(email_file, "r", encoding="utf-8") as file:
            email_content = file.read()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Extract the sender's email: {email_content}"}]
        )

        extracted_email = response.choices[0].message.content.strip()
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(extracted_email)

        return f"✅ Extracted email saved to {output_file}: {extracted_email}"

    except Exception as e:
        return f"❌ Error extracting email: {e}"
