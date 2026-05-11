class UI:
    def __init__(self, controller):
        self.controller = controller

    def submit_research_output(self, data):
        self.controller.submit(data)