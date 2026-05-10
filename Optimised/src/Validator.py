class Validator:
    def validate(self, data):
        # perform format validation
        return True if "title" in data else False

    def reject_submission(self):
        return "Rejected: Invalid format"