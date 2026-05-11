from metrics import call_counter
import metrics
class ReviewerManager:
    def filter_conflicts(self, reviewer_list):
        metrics.call_counter += 1
        print("ReviewerManager: Filtering conflicts...")
        return reviewer_list

    def check_workload(self, reviewer_list):
        metrics.call_counter += 1
        print("ReviewerManager: Checking workload...")
        return reviewer_list

    def assign_review(self, reviewer):
        metrics.call_counter += 1
        print("ReviewerManager: Assigning reviewer...")