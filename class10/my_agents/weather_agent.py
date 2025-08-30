from agents import Agent, function_tool

@function_tool
def find_weather(city: str) -> str:
    return f"""{city} temperature is 35 degree"""


weather_agent = Agent(
    name="WeatherAgent",
    instructions="""You are a weather agent. use tool find_weather 
    to get the weather of provided city""",
    handoff_description="get the weather of provided city",
    tools=[find_weather],
)
