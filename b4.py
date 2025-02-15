import os
import subprocess

# Define data directory for Git operations
DATA_DIR = "./data/git_repos/"

def run_task(repo_url: str, commit_msg: str):
    """Clones a Git repository, creates a commit, and pushes changes."""
    try:
        # Validate repository URL
        if not repo_url.startswith("https://"):
            return "❌ Invalid repository URL. Only HTTPS URLs are allowed."

        # Create target directory
        os.makedirs(DATA_DIR, exist_ok=True)

        # Extract repo name from URL
        repo_name = repo_url.rstrip("/").split("/")[-1].replace(".git", "")
        repo_path = os.path.join(DATA_DIR, repo_name)

        # Clone the repository if it doesn't exist
        if not os.path.exists(repo_path):
            subprocess.run(["git", "clone", repo_url, repo_path], check=True)
        else:
            return f"⚠️ Repository '{repo_name}' already cloned."

        # Create a test file
        test_file = os.path.join(repo_path, "test_file.txt")
        with open(test_file, "w") as file:
            file.write("This is a test commit for the LLM-based automation agent.\n")

        # Commit and push changes
        subprocess.run(["git", "-C", repo_path, "add", "."], check=True)
        subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "-C", repo_path, "push"], check=True)

        return f"✅ Repository '{repo_name}' cloned and changes committed with message: '{commit_msg}'"

    except subprocess.CalledProcessError as e:
        return f"❌ Git command failed: {e}"

    except Exception as e:
        return f"❌ Error during git operation: {e}"

# Debugging (if running this script directly)
if __name__ == "__main__":
    repo = input("Enter repository URL: ")
    message = input("Enter commit message: ")
    print(run_task(repo, message))
