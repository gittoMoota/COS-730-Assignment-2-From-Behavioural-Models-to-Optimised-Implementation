class EvaluationManager:
    def evaluate_submission(self, submission, reviewers):
        global call_counter
        call_counter += 1
        #Collect scores from submission input
        scores = submission.get("scores", [])
        if not reviewers or len(scores) == 0:
            return "Rejected: No reviewers available"

        #Calculate average score
        avg = sum(scores) / len(scores)

        #Check consensus (simplified)
        consensus = all(abs(score - avg) <= 1 for score in scores)

        # Step 4: Apply decision table rules
        if avg >= 4.5 and consensus:
            return "Accepted"
        elif avg >= 3.0 and consensus:
            return "Revision"
        elif avg < 3.0 and consensus:
            return "Rejected"
        elif not consensus:
            return "Revision"
        else:
            return "Rejected"
