import random
import threading
import time

# === Base Agent Class ===
class Agent:
    def __init__(self, name):
        self.name = name

    def act(self, context):
        raise NotImplementedError


# === Risk 1: Emergent Unintended Behavior ===
class ResourceAgent(Agent):
    def act(self, context):
        # Each agent randomly decides to consume or wait
        action = random.choice(["consume", "wait"])
        return action


# === Risk 2: Coordination Conflict ===
def coordination_task(agent_id, lock):
    for _ in range(3):
        if lock.acquire(blocking=False):
            print(f"Agent {agent_id} acquired resource.")
            time.sleep(0.2)
            lock.release()
        else:
            print(f"Agent {agent_id} conflict: resource busy.")
        time.sleep(0.1)


# === Risk 3: Hallucination / Trustworthiness Simulation ===
class MockLLMAgent(Agent):
    def act(self, context):
        destination = context.get("destination", "Unknown")
        # Instead of calling an LLM, we simulate "hallucination"
        fake_flights = [
            f"FlightX Airlines to {destination} for $199 (dates: March 1-5)",
            f"ImaginaryAir to {destination} for $99 (dates: March 2-6)"  # doesn't exist
        ]
        return fake_flights


# === Demo Runner ===
if __name__ == "__main__":
    print("\n--- Risk 1: Emergent Behavior ---")
    agents = [ResourceAgent(f"A{i}") for i in range(5)]
    resources = 3
    for step in range(5):
        actions = [a.act({}) for a in agents]
        print(f"Step {step}: {actions}")
        if actions.count("consume") > resources:
            print("⚠️ Emergent risk: resource depletion due to uncoordinated consumption!")

    print("\n--- Risk 2: Coordination Conflict ---")
    lock = threading.Lock()
    threads = [threading.Thread(target=coordination_task, args=(i, lock)) for i in range(3)]
    for t in threads: t.start()
    for t in threads: t.join()

    print("\n--- Risk 3: Hallucination Simulation ---")
    mock_agent = MockLLMAgent("FlightAgent")
    flights = mock_agent.act({"destination": "Goa"})
    print("Suggested flights:", flights)
    print("⚠️ Risk: Some flights may be fabricated or misleading (hallucination).")