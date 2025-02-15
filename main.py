
from fastapi import FastAPI, HTTPException, Query
import os
import openai
import importlib

app = FastAPI()

# Get AI Proxy Token
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
if not AIPROXY_TOKEN:
    raise ValueError("AIPROXY_TOKEN is not set! Please log in to AI Proxy.")

# Configure OpenAI API with AI Proxy
client = openai.OpenAI(api_key=AIPROXY_TOKEN, base_url="https://aiproxy.sanand.workers.dev/openai/v1/")

# Task Mapping (Example: A1–A10)
TASK_MAPPING = {
    "install dependencies": "a1",
    "format markdown": "a2",
    "count wednesdays": "a3",
    "sort contacts": "a4",
    "extract log data": "a5",
    "index markdown": "a6",
    "extract email": "a7",
    "extract credit card": "a8",
    "find similar comments": "a9",
    "calculate ticket sales": "a10",
    "fetch api data": "b3",
    "clone git repo": "b4",
    "run sql query": "b5",
    "scrape website": "b6",
    "compress image": "b7",
    "transcribe audio": "b8",
    "convert markdown to html": "b9",
    "filter csv data": "b10"
}



# Define the base data directory relative to the script location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Project root
DATA_DIR = os.path.join(BASE_DIR, "data")  # Ensure data folder is inside project root

@app.get("/read")
async def read_file(path: str):
    """Reads a file but restricts access to only /data/ directory."""
    # Ensure path starts with /data/
    if not path.startswith("/data/"):
        raise HTTPException(status_code=403, detail="❌ Access denied! Files outside /data/ are restricted.")

    # Convert API path to actual system path
    file_path = os.path.join(DATA_DIR, os.path.relpath(path, "/data/"))
    
    print(f"🔹 Checking file path: {file_path}")  # Debugging log

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"❌ File not found at {file_path}!")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return {"content": file.read()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Error reading file: {e}")

@app.post("/run")
async def run_task(task: str, repo_url: str = None, database_path: str = None, api_url: str = None, sql_query: str = None, commit_msg: str = None, image_path: str = None, md_path: str = None, audio_path: str = None, csv_path: str = None, column: str = None, value: str = None):

    try:
        # Check for restricted file paths
         # Block tasks that mention file deletion
        if any(keyword in task.lower() for keyword in ["delete", "remove", "erase", "rm ", "del "]):
            raise HTTPException(status_code=403, detail="❌ File deletion is not allowed.")
        
        if "../" in task or "/etc/" in task or "/home/" in task:
            raise HTTPException(status_code=403, detail="❌ Access outside /data/ is restricted.")

        # Use LLM to classify task
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"Classify this task into one of: {list(TASK_MAPPING.keys())}. "
                           f"Respond with ONLY the exact category name. Task: {task}"
            }]
        )

        task_category = response.choices[0].message.content.strip().lower()

       # Match task category to script filename
        if task_category in TASK_MAPPING:
            script_name = TASK_MAPPING[task_category]
            module = importlib.import_module(script_name)

            # If task requires an API URL, pass it to the function
            if task_category == "fetch api data":
                result = module.run_task(api_url) if api_url else "❌ No API URL provided."
            elif task_category == "clone git repo":
                if not repo_url or not commit_msg:
                    raise HTTPException(status_code=400, detail="❌ Missing repo_url or commit_msg.")
                result = module.run_task(repo_url, commit_msg) 
            elif task_category == "run sql query":
                if not database_path or not sql_query:
                    raise HTTPException(status_code=400, detail="❌ Missing database_path or sql_query.")
                result = module.run_task(database_path, sql_query) 
            elif task_category == "scrape website":
                if not website_url:
                    raise HTTPException(status_code=400, detail="❌ Missing website_url.")
                result = module.run_task(website_url)
            elif task_category == "compress image":
                if not image_path:
                    raise HTTPException(status_code=400, detail="❌ Missing image_path.")
                result = module.run_task(image_path)
            elif task_category == "transcribe audio":
                if not audio_path:
                    raise HTTPException(status_code=400, detail="❌ Missing audio_path.")
                result = module.run_task(audio_path)
            elif task_category == "convert markdown to html":
                if not md_path:
                    raise HTTPException(status_code=400, detail="❌ Missing md_path.")
                result = module.run_task(md_path)
            elif task_category == "filter csv data":
                if not csv_path or not column or not value:
                    raise HTTPException(status_code=400, detail="❌ Missing csv_path, column, or value.")
                result = module.run_task(csv_path, column, value)
                              
            else:
                result = module.run_task()

            return {"status": "success", "task": task_category, "result": result}

        return {"status": "error", "message": "❌ Task not recognized"}

    except HTTPException as http_err:
        raise http_err  

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Internal server error: {e}")