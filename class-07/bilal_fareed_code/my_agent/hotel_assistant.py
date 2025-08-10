from agents import Agent
from my_config.gemini_confg import MODEL
from guardrial_function.guardrial_input_function import guardrial_input_function

hotel_assistant = Agent(
    name="Hotel Customer care",
    instructions="""
    You are helpful hotel customer care assistant. hotel total room 200.
        - Hotel name is Hotel Sannata.
        - Hotel Owner name is Mr. Ratan Lal
        - 20 rooms not available for public, Its for special guest.
""",
    model=MODEL,
    input_guardrails=[guardrial_input_function],
    output_guardrails=[]
)
