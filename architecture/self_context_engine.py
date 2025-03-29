# Self-Context Engine (core loop)
class SelfContextEngine:
    def __init__(self, memory_nexus, signal_map):
        self.memory_nexus = memory_nexus
        self.signal_map = signal_map
        self.current_state = {}

    def update_context(self, input_signal):
        memory_trace = self.memory_nexus.query(input_signal)
        reinforced_goals = self.signal_map.reinforce(memory_trace)
        self.current_state = {
            "input": input_signal,
            "memory_trace": memory_trace,
            "reinforced_goals": reinforced_goals
        }
        return self.current_state

