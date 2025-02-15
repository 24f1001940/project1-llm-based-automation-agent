import os
import sqlite3
import json

# Define output file
OUTPUT_FILE = "./data/sql_query_result.json"

def run_task(database_path: str, sql_query: str):
    """Executes a SQL query on a SQLite database and saves the result to /data/sql_query_result.json."""
    try:
        # Validate that database_path is within /data/
        if not database_path.startswith("./data/"):
            return "❌ Access denied! Database must be inside /data/."

        # Check if the database file exists
        if not os.path.exists(database_path):
            return f"❌ Database file not found: {database_path}"

        # Execute the query
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute(sql_query)

        # Fetch results
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        # Convert results to a list of dictionaries
        results_dict = [dict(zip(columns, row)) for row in results]

        # Save results to JSON
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            json.dump(results_dict, file, indent=4)

        conn.close()
        return f"✅ SQL query executed successfully. Results saved to {OUTPUT_FILE}"

    except sqlite3.OperationalError as e:
        return f"❌ SQL error: {e}"
    except Exception as e:
        return f"❌ Error executing SQL query: {e}"

# Debugging (if running this script directly)
if __name__ == "__main__":
    db_path = input("Enter database path (e.g., ./data/ticket-sales.db): ")
    query = input("Enter SQL query: ")
    print(run_task(db_path, query))
