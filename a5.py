# import os
# import glob

# # Define log directory
# log_dir = "./data/logs/"
# output_file = "./data/logs-recent.txt"

# # Get list of all .log files sorted by modified time (most recent first)
# log_files = sorted(glob.glob(os.path.join(log_dir, "*.log")), key=os.path.getmtime, reverse=True)[:10]

# # Read the first line of each file
# first_lines = []
# for log_file in log_files:
#     with open(log_file, "r", encoding="utf-8") as f:
#         first_line = f.readline().strip()
#         first_lines.append(first_line)

# # Write the extracted lines to logs-recent.txt
# with open(output_file, "w", encoding="utf-8") as f:
#     f.write("\n".join(first_lines))

# print("Extracted first lines from the 10 most recent log files.")

import os
import glob

log_dir = "./data/logs/"
output_file = "./data/logs-recent.txt"

def run_task():
    """Extracts the first lines from the 10 most recent log files and saves them."""
    try:
        log_files = sorted(glob.glob(os.path.join(log_dir, "*.log")), key=os.path.getmtime, reverse=True)[:10]

        first_lines = []
        for log_file in log_files:
            with open(log_file, "r", encoding="utf-8") as f:
                first_lines.append(f.readline().strip())

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(first_lines))

        return f"✅ Extracted first lines from {len(first_lines)} log files. Saved to {output_file}."

    except Exception as e:
        return f"❌ Error extracting logs: {e}"
