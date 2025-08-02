from agents import Agent, ModelSettings
from my_config.gemini_confg import MODEL
from my_tool.math_tools import plus,multiply, subtract
from agents.agent import StopAtTools

math_agent = Agent(
    name="MAth Teacher", 
    instructions="you are my helpful math teacher.",
    model=MODEL,
    tools=[plus,multiply, subtract],
    tool_use_behavior=StopAtTools(stop_at_tool_names=["multiply", "subtract"]),
    # tool_use_behavior="stop_on_first_tool",
    # tool_use_behavior="run_llm_again",
    model_settings=ModelSettings(tool_choice="required"),
    # reset_tool_choice=True #default value True
    )
