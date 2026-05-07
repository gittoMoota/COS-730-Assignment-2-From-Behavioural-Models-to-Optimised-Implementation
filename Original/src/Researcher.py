class Researcher:
    def __init__(self, ui):
        self.ui = ui

    def submit_research_output(self, data):
        self.ui.submit_research_output(data)