class ClockInController:
    def __init__(self, state, time_service, state_service):
         self.state = state
         self.time_service = time_service
         self.state_service = state_service