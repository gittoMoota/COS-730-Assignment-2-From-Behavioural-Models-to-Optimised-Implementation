from Validator import Validator
from Database import Database
from ReviewerManager import ReviewerManager
from EvaluationManager import EvaluationManager
from NotificationService import NotificationService
from metrics import call_counter
import metrics


class SubmissionController:
    def submit(self, data):
        metrics.call_counter += 1
        
        validator = Validator()
        if not validator.validate(data):
            return validator.reject_submission()
        
        db = Database()
        db.save_submission(data)

        reviewer_manager = ReviewerManager()
        assigned_reviewers = reviewer_manager.assign_reviewers(data)

        evaluation_manager = EvaluationManager()
        outcome = evaluation_manager.evaluate_submission(data, assigned_reviewers)

        notification_service = NotificationService()
        return notification_service.send_notification(outcome)
    
    

