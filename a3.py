# from datetime import datetime
# import dateutil.parser

# # Function to parse a date in different formats
# def parse_date(date_str):
#     try:
#         return dateutil.parser.parse(date_str).date()  # Automatically detects format
#     except ValueError:
#         return None  # Skip if parsing fails

# # Read dates from file
# with open("./data/dates.txt", "r") as file:
#     dates = file.readlines()

# # Count Wednesdays
# wednesday_count = sum(1 for date in dates if parse_date(date.strip()) and parse_date(date.strip()).weekday() == 2)

# # Write the count to an output file
# with open("dates-wednesdays.txt", "w") as file:
#     file.write(str(wednesday_count))

# print(f"Total Wednesdays: {wednesday_count}")
import dateutil.parser

def run_task():
    """Counts Wednesdays in /data/dates.txt and saves to /data/dates-wednesdays.txt"""
    dates_file = "./data/dates.txt"
    output_file = "./data/dates-wednesdays.txt"

    try:
        with open(dates_file, "r", encoding="utf-8") as file:
            dates = [line.strip() for line in file.readlines() if line.strip()]

        wednesday_count = sum(1 for date in dates if dateutil.parser.parse(date).weekday() == 2)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(str(wednesday_count))

        return f"Wednesdays counted: {wednesday_count}"

    except Exception as e:
        return f"Error processing dates: {e}"
