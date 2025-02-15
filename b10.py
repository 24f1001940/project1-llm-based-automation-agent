import os
import pandas as pd
import json

# Define output file
OUTPUT_FILE = "./data/filtered_data.json"

def run_task(csv_path: str, column: str, value: str):
    """Filters a CSV file based on a column and value, then saves as JSON."""
    try:
        # Validate that CSV path is within /data/
        if not csv_path.startswith("./data/"):
            return "❌ Access denied! CSV files must be inside /data/."

        # Check if the CSV file exists
        if not os.path.exists(csv_path):
            return f"❌ CSV file not found: {csv_path}"

        # Read CSV file
        df = pd.read_csv(csv_path)

        # Validate column name
        if column not in df.columns:
            return f"❌ Column '{column}' not found in CSV."

        # Filter data
        filtered_df = df[df[column].astype(str) == value]

        # Convert to JSON
        result = filtered_df.to_dict(orient="records")

        # Save to file
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)

        return {"status": "success", "message": f"✅ Filtered data saved as {OUTPUT_FILE}", "data": result}

    except Exception as e:
        return {"status": "error", "message": f"❌ Error processing CSV: {e}"}

# Debugging (if running this script directly)
if __name__ == "__main__":
    path = input("Enter CSV file path (e.g., ./data/sample.csv): ")
    col = input("Enter column name: ")
    val = input("Enter filter value: ")
    print(run_task(path, col, val))
