from agents import Agent
from my_config.gemini_confg import MODEL
from my_tool.mw_tools import plus, subtract
from instruction.assistant_instruction import dynamic_instruction

assistant = Agent(
    name="Assistant",
    instructions=dynamic_instruction,
    model=MODEL,
    tools=[plus,subtract]
)

# print(assistant.tools)