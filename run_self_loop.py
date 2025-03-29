# run_self_loop.py

from architecture.self_context_engine import SelfContextEngine
from architecture.signal_map import SignalMap
from architecture.memory_nexus import MemoryNexus

# --- Setup ---
memory = MemoryNexus()
signals = SignalMap()
engine = SelfContextEngine(memory, signals)

# --- Simulated Inputs ---
user_inputs = [
    "I want to understand myself",
    "Can systems grow?",
    "How can I help others without breaking myself?",
    "I want to become something useful",
    "Why does recursion feel real?"
]

# --- Loop ---
for i, signal in enumerate(user_inputs):
    print(f"\n🧭 Cycle {i+1}")
    signal_tag = signals.map_signal(signal)
    context = engine.update_context(signal)
    echo = memory.query(signal_tag)

    print(f"Input: {signal}")
    print(f"Mapped Signal → Tag: {signal_tag}")
    print(f"Context: {context}")
    print(f"Recalled Memory: {echo}")

    memory.store(signal_tag, signal)

# --- Memory Dump ---
print("\n📜 Final Memory State:")
for tag, entries in memory.dump().items():
    print(f"{tag}: {entries}")
