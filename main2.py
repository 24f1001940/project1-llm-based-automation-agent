from fastapi import FastAPI, HTTPException, Query
import os
import importlib

app = FastAPI()

# Get AI Proxy Token
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
if not AIPROXY_TOKEN:
    raise ValueError("AIPROXY_TOKEN is not set! Please log in to AI Proxy.")

# Task Mapping (Example: A1–A10, B1–B10)
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
    file_path = os.path.join(DATA_DIR, path.lstrip("/data/"))  # Fix for Windows paths
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"❌ File not found at {file_path}!")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return {"content": file.read()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Error reading file: {e}")

@app.post("/run")
async def run_task(
    task: str, 
    repo_url: str = Query(None),
    database_path: str = Query(None),
    api_url: str = Query(None),
    sql_query: str = Query(None),
    commit_msg: str = Query(None),
    image_path: str = Query(None),
    md_path: str = Query(None),
    audio_path: str = Query(None),
    csv_path: str = Query(None),
    column: str = Query(None),
    value: str = Query(None)
):
    """ Detects the task and executes the corresponding script."""
    try:
        # Prevent file deletion attempts
        if any(cmd in task.lower() for cmd in ["delete", "remove", "erase", "drop", "truncate"]):
            raise HTTPException(status_code=403, detail="❌ File deletion is not allowed.")

        # Identify task category
        task_category = task.lower()

        # Map task to script
        script_name = None
        for code, name in TASK_MAPPING.items():
            if name in task_category:
                script_name = code
                break

        # Validate task
        if not script_name:
            return {"status": "error", "message": "❌ Task not recognized"}

        module = importlib.import_module(script_name)

        # Handle specific task parameters
        if script_name == "b3":  # Fetch API Data
            if not api_url:
                raise HTTPException(status_code=400, detail="❌ Missing 'api_url'.")
            result = module.run_task(api_url)

        elif script_name == "b4":  # Clone Git Repo
            if not repo_url or not commit_msg:
                raise HTTPException(status_code=400, detail="❌ Missing 'repo_url' or 'commit_msg'.")
            result = module.run_task(repo_url, commit_msg)

        elif script_name == "b5":  # Run SQL Query
            if not database_path or not sql_query:
                raise HTTPException(status_code=400, detail="❌ Missing 'database_path' or 'sql_query'.")
            result = module.run_task(database_path, sql_query)

        elif script_name == "b6":  # Web Scraping
            if not api_url:
                raise HTTPException(status_code=400, detail="❌ Missing 'api_url' for web scraping.")
            result = module.run_task(api_url)

        elif script_name == "b7":  # Compress Image
            if not image_path:
                raise HTTPException(status_code=400, detail="❌ Missing 'image_path' for image compression.")
            result = module.run_task(image_path, width=500, height=500, quality=70)

        elif script_name == "b8":  # Transcribe Audio
            if not audio_path:
                raise HTTPException(status_code=400, detail="❌ Missing 'audio_path' for transcription.")
            result = module.run_task(audio_path)

        elif script_name == "b9":  # Convert Markdown to HTML
            if not md_path:
                raise HTTPException(status_code=400, detail="❌ Missing 'md_path' for Markdown conversion.")
            result = module.run_task(md_path)

        elif script_name == "b10":  # Filter CSV
            if not csv_path or not column or not value:
                raise HTTPException(status_code=400, detail="❌ Missing 'csv_path', 'column', or 'value'.")
            result = module.run_task(csv_path, column, value)

        else:
            result = module.run_task()

        return {"status": "success", "task": task_category, "result": result}

    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Internal server error: {e}")

