call_counter = 0

from UI import UI
from SubmissionController import SubmissionController

def run_tests():
    ui = UI()

    #Use case 1: Invalid submission (missing title)
    print("Test 1: Invalid submission")
    result = ui.receive_submission({"content": "no title here"})
    print("Outcome:", result)

    #Use case 2: Valid submission but no reviewers
    print("\nTest 2: No reviewers available")
    # simulate ReviewerManager returning empty list
    result = ui.receive_submission({"title": "Research Output", "force_no_reviewers": True})
    print("Outcome:", result)

    #Use case 3: Valid submission with low scores
    print("\nTest 3: Low scores")
    result = ui.receive_submission({"title": "Research Output", "scores": [1, 2, 2]})
    print("Outcome:", result)

    #Use case 4: Valid submission with moderate scores
    print("\nTest 4: Moderate scores")
    result = ui.receive_submission({"title": "Research Output", "scores": [3, 3, 4]})
    print("Outcome:", result)

    #Use case 5: Valid submission with high scores
    print("\nTest 5: High scores")
    result = ui.receive_submission({"title": "Research Output", "scores": [5, 5, 4]})
    print("Outcome:", result)

if __name__ == "__main__":
    run_tests()
