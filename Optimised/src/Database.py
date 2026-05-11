from metrics import call_counter
import metrics
class Database:
    def save_submission(self, data):
        metrics.call_counter += 1

        print("Submission saved:", data)

    def fetch_and_filter_reviewers(self):
        metrics.call_counter += 1

        # simplified reviewer fetching
        return ["ReviewerA", "ReviewerB"]


