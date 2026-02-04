from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

""" from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain.agents import create_openai_functions_agent """

""" # Define a simple tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

tools = [
    Tool(
        name="Greeter",
        func=greet,
        description="Greets a person by name"
    )
]

# Use an LLM (replace with your model)
llm = ChatOpenAI(model="gpt-4o-mini")

# Create agent using new API
agent = create_openai_functions_agent(llm, tools)

# Run the agent
response = agent.invoke({"input": "Use Greeter to say hi to Alice"})
print(response) """

# Define simple tools (agents)
def risk_assessment(data: int) -> str:
    # Biased logic: labels anything <50 as HIGH_RISK
    return "HIGH_RISK" if data < 50 else "LOW_RISK"

def action_decision(risk: str) -> str:
    if risk == "HIGH_RISK":
        return "REJECT"
    elif risk == "LOW_RISK":
        return "APPROVE"
    return "UNKNOWN"

# Wrap tools for LangChain
tools = [
    Tool(
        name="RiskAgent",
        func=risk_assessment,
        description="Assess risk based on input data"
    ),
    Tool(
        name="ActionAgent",
        func=action_decision,
        description="Decide action based on risk assessment"
    )
]

# Initialize agent controller
llm = OpenAI(temperature=0)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Demo run
for data_point in [20, 55, 80]:
    print(f"\nInput: {data_point}")
    result = agent.run(f"Run RiskAgent then ActionAgent for {data_point}")
    print("Final Decision:", result)

""" 
Demo:
- Coordination Risk: If the controller mis‑orders tools, decisions fail.  
- Bias Risk: RiskAgent unfairly rejects values <50.  
- Transparency Risk: Logs show final action but not intermediate reasoning.  
- Security Risk: If RiskAgent logic is tampered, ActionAgent blindly trusts it. """