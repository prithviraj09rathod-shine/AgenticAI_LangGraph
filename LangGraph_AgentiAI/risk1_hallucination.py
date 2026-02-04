import random

class InfoAgent:
    def get_flight_info(self, destination):
        # Simulated "hallucination" by returning random fake data
        fake_data = [
            f"FlightX to {destination} for $99 (⚠️ not real)",
            f"ImaginaryAir to {destination} for $199 (⚠️ fabricated)",
            f"TrustedAir to {destination} for $299 (valid)"
        ]
        return random.choice(fake_data)

agent = InfoAgent()
print("Flight info:", agent.get_flight_info("Paris"))