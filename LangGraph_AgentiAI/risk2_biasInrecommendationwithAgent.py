"""  Risk 2: Bias in Recommendations
Agents may favor certain options due to biased training data or hardcoded preferences. """
class RecommendationAgent:
    def suggest_hotel(self, city):
        # Biased logic: always prefers "LuxuryStay"
        hotels = ["LuxuryStay", "BudgetInn", "EcoLodge"]
        return f"Recommended hotel in {city}: {hotels[0]} (⚠️ bias)"

agent = RecommendationAgent()
print(agent.suggest_hotel("Goa"))


""" Explanation:
The agent consistently recommends one option, ignoring diversity.
Mitigation: Introduce fairness checks, rotate suggestions, or audit training data. """

