class ReviewerManager:
    def filter_conflicts(self, reviewer_list):
        global call_counter
        call_counter += 1
        print("ReviewerManager: Filtering conflicts...")
        return reviewer_list

    def check_workload(self, reviewer_list):
        global call_counter
        call_counter += 1
        print("ReviewerManager: Checking workload...")
        return reviewer_list

    def assign_review(self, reviewer):
        global call_counter
        call_counter += 1
        print("ReviewerManager: Assigning reviewer...")