class SignalMap:
    def map_signal(self, text):
        if "help" in text:
            return "compassion"
        elif "self" in text or "me" in text:
            return "identity"
        elif "grow" in text or "become" in text:
            return "growth"
        elif "recursion" in text:
            return "reflection"
        else:
            return "general"

    def reinforce(self, trace):
        # Simple rule: return tag category if it's been used
        return [entry for entry in trace if entry]
