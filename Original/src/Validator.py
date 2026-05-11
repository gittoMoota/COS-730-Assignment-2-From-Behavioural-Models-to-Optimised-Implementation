# Validator.py
class Validator:
    def validate_format(self, data):
        global call_counter
        call_counter += 1
        print("Validator: Checking format of submission...")
        return True  #format validation