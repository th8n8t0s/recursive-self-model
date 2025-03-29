# architecture/self_context_engine.py

class SelfContextEngine:
    def __init__(self, memory_nexus, signal_map, logger=None):
        self.memory_nexus = memory_nexus
        self.signal_map = signal_map
        self.current_state = {}
        self.logger = logger

    def update_context(self, input_signal):
        # Retrieve relevant memory entries
        memory_trace = self.memory_nexus.query(input_signal)

        # Apply signal reinforcement (pattern activation)
        reinforced_goals = self.signal_map.reinforce(memory_trace)

        # Update current active context
        self.current_state = {
            "input": input_signal,
            "memory_trace": memory_trace,
            "reinforced_goals": reinforced_goals
        }

        # Optional: log context state
        if self.logger:
            self.logger.log_context(self.current_state)

        return self.current_state

    def summarize(self):
        return {
            "active_goals": self.current_state.get("reinforced_goals", []),
            "last_signal": self.current_state.get("input")
        }
