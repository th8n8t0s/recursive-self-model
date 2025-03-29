# memory_nexus.py
from collections import defaultdict

class MemoryNexus:
    def __init__(self):
        self.memory = defaultdict(list)

    def store(self, tag, thought):
        self.memory[tag].append(thought)

    def recall(self, tag):  # <-- THIS is the method you need
        entries = self.memory[tag]
        return entries[-1] if entries else "No past reflection found."

    def dump(self):
        return self.memory
