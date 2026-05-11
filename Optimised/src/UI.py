from SubmissionController import SubmissionController
class UI:
    def receive_submission(self, data):
        controller = SubmissionController()
        return controller.submit(data)
