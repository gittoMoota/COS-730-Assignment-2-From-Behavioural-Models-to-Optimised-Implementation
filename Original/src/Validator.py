from metrics import call_counter
import metrics
class Validator:
    def validate_format(self, data):
        metrics.call_counter += 1
        print("Validator: Checking format of submission...")
        return True  #format validation