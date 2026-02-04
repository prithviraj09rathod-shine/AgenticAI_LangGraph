import os
from openai import OpenAI

# Initialize OpenAI client (set your API key in environment variable)
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



# === Base Agent Class ===
class Agent:
    def __init__(self, name: str):
        self.name = name

    def query_llm(self, prompt: str) -> str:
        """Helper to call LLM with a prompt."""
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-4o" / Azure deployment name
            messages=[{"role": "system", "content": f"You are {self.name}, a travel assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=300
        )
        return response.choices[0].message.content

    def act(self, task: str, context: dict) -> dict:
        raise NotImplementedError


# === Specialized Agents ===
class FlightAgent(Agent):
    def act(self, task: str, context: dict) -> dict:
        destination = context.get("destination", "Unknown")
        prompt = f"Suggest 2 flight options to {destination} with airline, price, and dates."
        flights = self.query_llm(prompt)
        return {"flights": flights, "agent": self.name}


class HotelAgent(Agent):
    def act(self, task: str, context: dict) -> dict:
        destination = context.get("destination", "Unknown")
        prompt = f"Suggest 2 hotel options in {destination} with name, price per night, and rating."
        hotels = self.query_llm(prompt)
        return {"hotels": hotels, "agent": self.name}


class RecommendationAgent(Agent):
    def act(self, task: str, context: dict) -> dict:
        destination = context.get("destination", "Unknown")
        prompt = f"Suggest 3 fun activities or attractions in {destination}."
        activities = self.query_llm(prompt)
        return {"activities": activities, "agent": self.name}


class RiskMonitorAgent(Agent):
    def act(self, task: str, context: dict) -> dict:
        prompt = f"""Analyze the following trip plan for risks:
        Flights: {context.get('flights')}
        Hotels: {context.get('hotels')}
        Activities: {context.get('activities')}
        Identify conflicts (like date mismatches, budget issues) and return warnings."""
        risks = self.query_llm(prompt)
        return {"risks": risks, "agent": self.name}


# === Planner Agent ===
class PlannerAgent(Agent):
    def __init__(self, name: str, sub_agents: dict, risk_agent: Agent):
        super().__init__(name)
        self.sub_agents = sub_agents
        self.risk_agent = risk_agent

    def act(self, task: str, context: dict) -> dict:
        print(f"[{self.name}] Coordinating trip planning for {context['destination']}...")

        # Call sub-agents
        flight_info = self.sub_agents["flight"].act(task, context)
        hotel_info = self.sub_agents["hotel"].act(task, context)
        rec_info = self.sub_agents["recommendation"].act(task, context)

        # Aggregate results
        plan = {
            "destination": context["destination"],
            "flights": flight_info["flights"],
            "hotels": hotel_info["hotels"],
            "activities": rec_info["activities"]
        }

        # Run risk monitor
        risk_report = self.risk_agent.act(task, plan)
        plan["risks"] = risk_report["risks"]

        return {"trip_plan": plan, "agent": self.name}


# === Run System ===
if __name__ == "__main__":
    flight_agent = FlightAgent("FlightAgent")
    hotel_agent = HotelAgent("HotelAgent")
    rec_agent = RecommendationAgent("RecommendationAgent")
    risk_agent = RiskMonitorAgent("RiskMonitorAgent")

    planner = PlannerAgent("PlannerAgent", {
        "flight": flight_agent,
        "hotel": hotel_agent,
        "recommendation": rec_agent
    }, risk_agent)

    user_context = {"destination": "Goa", "dates": "March 2026"}
    trip_plan = planner.act("Plan my trip", user_context)

    print("\n=== Final Trip Plan with Risk Report ===")
    print(trip_plan)