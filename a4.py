# import json

# # Read the contacts.json file
# with open("./data/contacts.json", "r") as file:
#     contacts = json.load(file)  # Load JSON data as a list of dictionaries

# # Sort contacts by last_name, then first_name
# contacts_sorted = sorted(contacts, key=lambda x: (x["last_name"], x["first_name"]))

# # Write the sorted contacts to contacts-sorted.json
# with open("./data/contacts-sorted.json", "w") as file:
#     json.dump(contacts_sorted, file, indent=4)

# print("Sorting completed. Check contacts-sorted.json.")
import json
import os

# Define file paths
contacts_file = "./data/contacts.json"
output_file = "./data/contacts-sorted.json"

def run_task():
    """Reads /data/contacts.json, sorts contacts, and writes to /data/contacts-sorted.json"""
    try:
        # Read contacts from JSON file
        with open(contacts_file, "r", encoding="utf-8") as file:
            contacts = json.load(file)  # Load JSON data as a list of dictionaries

        # Sort contacts by last_name, then first_name
        contacts_sorted = sorted(contacts, key=lambda x: (x["last_name"], x["first_name"]))

        # Write the sorted contacts to output file
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(contacts_sorted, file, indent=4)

        return f"✅ Sorting completed. Check {output_file}"

    except Exception as e:
        return f"❌ Error sorting contacts: {e}"

# Debugging (if running this script directly)
if __name__ == "__main__":
    print(run_task())
