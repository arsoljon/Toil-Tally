class GraphController:
    def __init__ (self, state, week_service):
        self.state = state
        self.week_service = week_service

    def get_bar_info(self):
        return self.week_service.get_bar_info(self.state)