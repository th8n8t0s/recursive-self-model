# Signal Map (goal echo system)
class SignalMap:
    def __init__(self):
        self.signal_patterns = {}

    def reinforce(self, memory_trace):
        goals = {}
        for signal in memory_trace:
            if signal in self.signal_patterns:
                goals[signal] = self.signal_patterns[signal]
        return goals

    def add_signal(self, signal, meaning):
        self.signal_patterns[signal] = meaning

