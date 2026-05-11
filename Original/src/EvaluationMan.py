from metrics import call_counter
import metrics
class EvaluationManager:
    def calculate_average(self, scores):
        metrics.call_counter += 1
        print("EvaluationManager: Calculating average...")
        return 0

    def check_consensus(self, scores):
        metrics.call_counter += 1
        print("EvaluationManager: Checking consensus...")
        return True

    def apply_rules(self, average, consensus):
        metrics.call_counter += 1
        print("EvaluationManager: Applying rules...")
        return "accepted"