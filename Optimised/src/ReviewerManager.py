from Database import Database
class ReviewerManager:
    def assign_reviewers(self, submission):
        db = Database()
        reviewers = db.fetch_and_filter_reviewers()
        # filtering logic encapsulated here
        return reviewers