call_counter = 0

from Researcher import Researcher
from UI import UI
from SubmissionCtrler import SubmissionController
from Validator import Validator
from Database import Database
from ReviewerMan import ReviewerManager
from Reviewer import Reviewer
from EvaluationMan import EvaluationManager
from NotificationService import NotificationService

def main():
    #Instantiating collaborators
    validator = Validator()
    database = Database()
    reviewer_manager = ReviewerManager()
    evaluation_manager = EvaluationManager()
    notification_service = NotificationService()

    #Controller and UI
    controller = SubmissionController(validator, database, reviewer_manager, evaluation_manager, notification_service)
    ui = UI(controller)

    # Create researcher
    researcher = Researcher(ui)

    # Run baseline submission
    researcher.submit_research_output("Sample research data")

if __name__ == "__main__":
    main()
