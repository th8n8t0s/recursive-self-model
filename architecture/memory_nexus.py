from collections import defaultdict

class MemoryNexus:
    def __init__(self):
        self.memory = defaultdict(list)

    def store(self, tag, thought):
        self.memory[tag].append(thought)

    def query(self, input_signal):
        # Use keyword match to choose a memory tag
        if "help" in input_signal:
            tag = "compassion"
        elif "self" in input_signal or "me" in input_signal:
            tag = "identity"
        elif "grow" in input_signal or "become" in input_signal:
            tag = "growth"
        elif "recursion" in input_signal:
            tag = "reflection"
        else:
            tag = "general"
        return self.memory[tag]
