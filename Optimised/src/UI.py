from SubmissionController import SubmissionController
class UI:
    def receive_submission(self, data):
        global call_counter
        call_counter += 1
        controller = SubmissionController()
        return controller.submit(data)
