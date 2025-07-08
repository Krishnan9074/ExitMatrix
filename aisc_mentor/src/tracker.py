# Progress Tracking

import json
import os

PROGRESS_FILE = "user_progress.json"

def load_progress():
    """Loads user progress from a file."""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {} # Return empty dict if file is corrupted
    return {}

def save_progress(progress_data: dict):
    """Saves user progress to a file."""
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress_data, f, indent=4)

def complete_challenge(user_id: str, repo_id: str, unit_id: str):
    """Marks a challenge as completed for a user."""
    progress = load_progress()
    if user_id not in progress:
        progress[user_id] = {}
    if repo_id not in progress[user_id]:
        progress[user_id][repo_id] = []

    if unit_id not in progress[user_id][repo_id]:
        progress[user_id][repo_id].append(unit_id)
        save_progress(progress)
        print(f"Progress saved: User {user_id} completed {unit_id} in {repo_id}.")
    else:
        print(f"Challenge {unit_id} already completed by {user_id} in {repo_id}.")

def get_completed_challenges(user_id: str, repo_id: str):
    """Gets a list of completed challenges for a user in a specific repo."""
    progress = load_progress()
    return progress.get(user_id, {}).get(repo_id, [])

if __name__ == '__main__':
    # Test progress tracking
    USER = "test_user"
    REPO = "test_repo"

    print(f"Initial progress for {USER} in {REPO}: {get_completed_challenges(USER, REPO)}")

    complete_challenge(USER, REPO, "unit_A")
    complete_challenge(USER, REPO, "unit_B")
    complete_challenge(USER, REPO, "unit_A") # Try completing again

    print(f"Final progress for {USER} in {REPO}: {get_completed_challenges(USER, REPO)}")

    # Clean up test file
    if os.path.exists(PROGRESS_FILE):
        os.remove(PROGRESS_FILE)
