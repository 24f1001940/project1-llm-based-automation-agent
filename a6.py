# import os
# import glob
# import json

# # Define base directory and output file
# docs_dir = "./data/docs/"
# output_file = "./data/docs/index.json"

# # Find all Markdown files recursively in all subfolders
# md_files = glob.glob(os.path.join(docs_dir, "**", "*.md"), recursive=True)

# # Dictionary to store filename → H1 mapping
# index_data = {}

# for md_file in md_files:
#     filename = os.path.relpath(md_file, docs_dir)  # Get relative path inside /docs
#     print(f"Processing: {filename}")  # Debugging line

#     with open(md_file, "r", encoding="utf-8") as f:
#         found_heading = False
#         for line in f:
#             if line.startswith("# "):  # First H1 heading found
#                 index_data[filename] = line[2:].strip()  # Remove "# " from heading
#                 found_heading = True
#                 break  # Stop after first H1 heading
        
#         if not found_heading:
#             print(f"⚠️ No H1 heading found in {filename}")

# # Save index to index.json
# with open(output_file, "w", encoding="utf-8") as f:
#     json.dump(index_data, f, indent=4)

# print(f"\n✅ Index created: {output_file} → {len(index_data)} entries")

import os
import glob
import json

docs_dir = "./data/docs/"
output_file = "./data/docs/index.json"

def run_task():
    """Indexes Markdown files and extracts the first H1 heading from each."""
    try:
        md_files = glob.glob(os.path.join(docs_dir, "**", "*.md"), recursive=True)
        index_data = {}

        for md_file in md_files:
            filename = os.path.relpath(md_file, docs_dir)
            with open(md_file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("# "):
                        index_data[filename] = line[2:].strip()
                        break  # Stop after first H1 heading

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(index_data, f, indent=4)

        return f"✅ Index created: {len(index_data)} entries saved to {output_file}."

    except Exception as e:
        return f"❌ Error indexing Markdown files: {e}"
