# import sqlite3

# # Define database and output file paths
# db_path = "./data/ticket-sales.db"
# output_file = "./data/ticket-sales-gold.txt"

# # Connect to the SQLite database
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# # Execute query to calculate total sales for "Gold" tickets
# cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'")
# total_sales = cursor.fetchone()[0]

# # If no sales data, set total to 0
# if total_sales is None:
#     total_sales = 0

# # Save the total sales to a text file
# with open(output_file, "w", encoding="utf-8") as file:
#     file.write(str(total_sales))

# # Close database connection
# conn.close()

# print(f"✅ Total sales for 'Gold' tickets saved to {output_file}: {total_sales}")

import sqlite3

db_path = "./data/ticket-sales.db"
output_file = "./data/ticket-sales-gold.txt"

def run_task():
    """Calculates total sales for 'Gold' ticket type and saves it."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'")
        total_sales = cursor.fetchone()[0] or 0

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(str(total_sales))

        conn.close()
        return f"✅ Total sales for 'Gold' tickets saved to {output_file}: {total_sales}"

    except Exception as e:
        return f"❌ Error calculating ticket sales: {e}"
