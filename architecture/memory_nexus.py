# Memory Nexus (context linking)
class MemoryNexus:
    def __init__(self):
        self.log = []

    def store(self, signal):
        self.log.append(signal)

    def query(self, signal):
        return [entry for entry in self.log if signal in entry]
