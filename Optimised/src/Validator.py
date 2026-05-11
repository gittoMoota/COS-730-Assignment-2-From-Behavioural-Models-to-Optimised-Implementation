from metrics import call_counter
import metrics
class Validator:
    def validate(self, data):
        metrics.call_counter += 1
        #format validation
        return True if "title" in data else False

    def reject_submission(self):
        metrics.call_counter += 1
        return "Rejected: Invalid format"