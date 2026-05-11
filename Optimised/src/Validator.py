class Validator:
    def validate(self, data):
        global call_counter
        call_counter += 1
        # perform format validation
        return True if "title" in data else False

    def reject_submission(self):
        global call_counter
        call_counter += 1
        return "Rejected: Invalid format"