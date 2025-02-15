# import os
# import openai
# import json
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity

# # Get AI Proxy Token
# AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
# if not AIPROXY_TOKEN:
#     raise ValueError("AIPROXY_TOKEN is not set! Please log in to AI Proxy.")

# AIPROXY_TOKEN = AIPROXY_TOKEN.strip()

# print(f"AIPROXY_TOKEN: {repr(AIPROXY_TOKEN)}")  

# # Configure OpenAI API with AI Proxy
# client = openai.OpenAI(api_key=AIPROXY_TOKEN, base_url="https://aiproxy.sanand.workers.dev/openai/v1/")

# # Define file paths
# comments_file = "./data/comments.txt"
# output_file = "./data/comments-similar.txt"

# # Read comments from file
# with open(comments_file, "r", encoding="utf-8") as file:
#     comments = [line.strip() for line in file.readlines() if line.strip()]

# if len(comments) < 2:
#     raise ValueError("Not enough comments to find similarity.")

# # Get embeddings for all comments
# response = client.embeddings.create(
#     model="text-embedding-3-small",
#     input=comments
# )

# # Extract embeddings
# embeddings = np.array([item.embedding for item in response.data])

# # Compute pairwise cosine similarity
# similarity_matrix = cosine_similarity(embeddings)

# # Find the most similar pair (excluding self-similarity)
# np.fill_diagonal(similarity_matrix, 0)  # Ignore self-matching
# i, j = np.unravel_index(np.argmax(similarity_matrix), similarity_matrix.shape)

# # Save the most similar comments
# with open(output_file, "w", encoding="utf-8") as file:
#     file.write(f"{comments[i]}\n{comments[j]}")

# print(f"✅ Most similar comments saved to {output_file}:")
# print(f"- {comments[i]}")
# print(f"- {comments[j]}")

import os
import openai
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN", "").strip()
if not AIPROXY_TOKEN:
    raise ValueError("AIPROXY_TOKEN is not set! Please log in to AI Proxy.")

client = openai.OpenAI(api_key=AIPROXY_TOKEN, base_url="https://aiproxy.sanand.workers.dev/openai/v1/")
comments_file = "./data/comments.txt"
output_file = "./data/comments-similar.txt"

def run_task():
    """Finds the most similar pair of comments based on embeddings."""
    try:
        with open(comments_file, "r", encoding="utf-8") as file:
            comments = [line.strip() for line in file.readlines() if line.strip()]

        if len(comments) < 2:
            return "❌ Not enough comments to find similarity."

        response = client.embeddings.create(model="text-embedding-3-small", input=comments)
        embeddings = np.array([item.embedding for item in response.data])

        similarity_matrix = cosine_similarity(embeddings)
        np.fill_diagonal(similarity_matrix, 0)
        i, j = np.unravel_index(np.argmax(similarity_matrix), similarity_matrix.shape)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(f"{comments[i]}\n{comments[j]}")

        return f"✅ Most similar comments saved to {output_file}."

    except Exception as e:
        return f"❌ Error finding similar comments: {e}"
