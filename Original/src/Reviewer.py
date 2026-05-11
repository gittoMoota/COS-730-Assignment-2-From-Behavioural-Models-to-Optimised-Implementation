class Reviewer:
    def save_score(self, score):
        global call_counter
        call_counter += 1
        print(f"Reviewer: Saving score {score}...")

    def submit_score(self, score):
        global call_counter
        call_counter += 1
        print(f"Reviewer: Submitting score {score}...")