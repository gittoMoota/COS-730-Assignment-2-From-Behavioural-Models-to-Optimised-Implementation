from Researcher import Researcher
from UI import UI
from SubmissionController import SubmissionController
from Validator import Validator
from Database import Database
from ReviewerManager import ReviewerManager
from EvaluationManager import EvaluationManager
from NotificationService import NotificationService
import metrics

def run_tests():
    ui = UI()

    #Use case 1: Invalid submission (missing title)
    print("Test 1: Invalid submission")
    result = ui.receive_submission({"content": "no title here"})
    print("Outcome:", result)
    print(f"Total method calls: {metrics.call_counter}")
    metrics.call_counter = 0


    #Use case 2: Valid submission but no reviewers
    print("\nTest 2: No reviewers available")
    # simulate ReviewerManager returning empty list
    result = ui.receive_submission({"title": "Research Output", "force_no_reviewers": True})
    print("Outcome:", result)
    print(f"Total method calls: {metrics.call_counter}")
    metrics.call_counter = 0


    #Use case 3: Valid submission with low scores
    print("\nTest 3: Low scores")
    result = ui.receive_submission({"title": "Research Output", "scores": [1, 2, 2]})
    print("Outcome:", result)
    print(f"Total method calls: {metrics.call_counter}")
    metrics.call_counter = 0


    #Use case 4: Valid submission with moderate scores
    print("\nTest 4: Moderate scores")
    result = ui.receive_submission({"title": "Research Output", "scores": [3, 3, 4]})
    print("Outcome:", result)
    
    print(f"Total method calls: {metrics.call_counter}")
    metrics.call_counter = 0

    
    #Use case 5: Valid submission with high scores
    print("\nTest 5: High scores")
    result = ui.receive_submission({"title": "Research Output", "scores": [5, 5, 4]})
    print("Outcome:", result)
    
    print(f"Total method calls: {metrics.call_counter}")
    metrics.call_counter = 0

if __name__ == "__main__":
    run_tests()
