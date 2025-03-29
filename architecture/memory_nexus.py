from collections import defaultdict

class MemoryNexus:
    def __init__(self):
        self.memory = defaultdict(list)

    def store(self, tag, thought):
        self.memory[tag].append(thought)

    def query(self, tag):
        return self.memory.get(tag, [])

    def dump(self):
        return self.memory
