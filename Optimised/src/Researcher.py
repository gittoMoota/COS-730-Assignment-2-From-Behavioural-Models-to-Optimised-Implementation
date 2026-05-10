class Researcher:
    def __init__(self, name):
        self.name = name

    def submit_output(self, data, ui):
        return ui.receive_submission(data)