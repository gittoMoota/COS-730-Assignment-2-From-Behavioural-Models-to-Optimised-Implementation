class SubmissionController:
    def __init__(self, validator, database, reviewer_manager, evaluation_manager, notification_service):
        self.validator = validator
        self.database = database
        self.reviewer_manager = reviewer_manager
        self.evaluation_manager = evaluation_manager
        self.notification_service = notification_service

    def submit(self, data):
        # Step 1: Validate format
        valid = self.validator.validate_format(data)
        if not valid:
            # Invalid submission → notify researcher
            self.notification_service.send_notification("Error: Invalid format")
            return

        # Step 2: Save submission
        self.database.save_submission(data)

        # Step 3: Fetch reviewers
        reviewer_list = self.database.fetch_reviewers()

        # Step 4: Filter conflicts and workload
        reviewer_list = self.reviewer_manager.filter_conflicts(reviewer_list)
        reviewer_list = self.reviewer_manager.check_workload(reviewer_list)

        # Step 5: Assign reviewers (loop)
        for reviewer in reviewer_list:
            self.reviewer_manager.assign_review(reviewer)
            # Reviewer saves and submits score (placeholders for now)
            reviewer.save_score(0)
            reviewer.submit_score(0)

        # Step 6: Evaluation
        scores = [0 for _ in reviewer_list]  # placeholder scores
        average = self.evaluation_manager.calculate_average(scores)
        consensus = self.evaluation_manager.check_consensus(scores)
        result = self.evaluation_manager.apply_rules(average, consensus)

        # Step 7: Notify outcome
        if result == "accepted":
            self.notification_service.notify_acceptance()
            self.notification_service.send_notification("Submission accepted")
        elif result == "rejected":
            self.notification_service.notify_rejection()
            self.notification_service.send_notification("Submission rejected")
        elif result == "revision":
            self.notification_service.notify_revision()
            self.notification_service.send_notification("Revision required")
