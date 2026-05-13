from metrics import call_counter
import metrics
class Database:
    def save_submission(self, data):
        metrics.call_counter += 1
        print("Database: Saving submission...")

    def fetch_reviewers(self):
        metrics.call_counter += 1
        print("Database: Fetching reviewers...")
        return []