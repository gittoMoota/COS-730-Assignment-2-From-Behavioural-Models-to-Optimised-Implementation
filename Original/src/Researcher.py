class Researcher:
    def __init__(self, ui):
        self.ui = ui

    def submit_research_output(self, data):
        global call_counter
        call_counter += 1
        self.ui.submit_research_output(data)