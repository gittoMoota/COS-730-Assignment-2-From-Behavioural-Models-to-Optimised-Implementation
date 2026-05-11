class UI:
    def __init__(self, controller):
        global call_counter
        call_counter += 1
        self.controller = controller

    def submit_research_output(self, data):
        global call_counter
        call_counter += 1
        self.controller.submit(data)