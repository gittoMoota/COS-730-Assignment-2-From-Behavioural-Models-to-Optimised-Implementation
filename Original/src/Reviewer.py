from metrics import call_counter
import metrics
class Reviewer:
    def save_score(self, score):
        metrics.call_counter += 1
        print(f"Reviewer: Saving score {score}...")

    def submit_score(self, score):
        metrics.call_counter += 1
        print(f"Reviewer: Submitting score {score}...")