from agents import Agent
from my_confg.gemini_confg import MODEL
from my_tool.my_tools import plus
from my_tool.weather_tool import fetch_weather




math_agent = Agent(
    name="math teacher",
    instructions="you are  math teacher and solve problem in one line",
    model=MODEL,
    tools=[plus,fetch_weather],
    # tool_use_behavior="stop_on_first_tool"         
                   )

math_tool = math_agent.as_tool(
    tool_name="math_specialize_agent",
    tool_description=None
)
assistant_agent = Agent(
    name="assitant",
    instructions="you are helpful assistant",
    model=MODEL,
    tools=[math_tool]
    )
