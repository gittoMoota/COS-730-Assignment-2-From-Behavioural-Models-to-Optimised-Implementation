class Researcher:
    def __init__(self, name):
        global call_counter
        call_counter += 1
        self.name = name

    def submit_output(self, data, ui):
        global call_counter
        call_counter += 1
        return ui.receive_submission(data)