# Database.py
class Database:
    def save_submission(self, data):
        global call_counter
        call_counter += 1
        print("Database: Saving submission...")

    def fetch_reviewers(self):
        global call_counter
        call_counter += 1
        print("Database: Fetching reviewers...")
        return []