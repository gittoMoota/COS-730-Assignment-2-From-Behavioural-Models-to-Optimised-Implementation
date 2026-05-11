class Database:
    def save_submission(self, data):
        global call_counter
        call_counter += 1

        print("Submission saved:", data)

    def fetch_and_filter_reviewers(self):
        global call_counter
        call_counter += 1

        # simplified reviewer fetching
        return ["ReviewerA", "ReviewerB"]


