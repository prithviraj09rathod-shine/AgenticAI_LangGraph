""" 
⚠️ Risk 3: Coordination Overhead
Multiple agents working independently can cause redundant calls and slow performance. """
import time

class PlannerAgent:
    def query_agents(self):
        start = time.time()
        # Each sub-agent queried sequentially (inefficient)
        time.sleep(0.5)  # FlightAgent
        time.sleep(0.5)  # HotelAgent
        time.sleep(0.5)  # ActivityAgent
        end = time.time()
        return f"Total time taken: {end - start:.2f} seconds"

planner = PlannerAgent()
print(planner.query_agents())

""" Summary of Top 5 Recurring Risks in AI Agents:
1. Hallucination → fabricated outputs mislead users.
2. Bias → skewed recommendations reduce fairness.
3. Privilege Compromise → agents gain unauthorized access.
4.Prompt injection attacks → hidden commands exploit agent trust.(malicious inputs manipulate agent behavior.)
5. Coordination Overhead → inefficient agent orchestration slows performance.
Together with Privilege Compromise and Prompt Injection, these form the five most recurring risks in AI agents."""