from Database import Database
from metrics import call_counter
import metrics

class ReviewerManager:
    def assign_reviewers(self, submission):
        metrics.call_counter += 1
        db = Database()
        reviewers = db.fetch_and_filter_reviewers()
        # filtering logic encapsulated here
        return reviewers