from pprint import pprint
from typing import Literal
from agents import (
    Agent,
    ModelSettings,
    Runner,
    RunConfig,
    function_tool,
)
from pydantic import BaseModel


from my_agents.weather_agent import weather_agent
from my_agents.hotel_agent import hotel_agent
from my_agents.flight_agent import flight_agent
from my_config import model
from agents.extensions import handoff_filters

import asyncio


@function_tool
def get_weather(city: str) -> str:
    "return the weather of provided city"
    return f"{city}:35 degree"


agent = Agent(
    "GeneralAgent",
    instructions="You are a helpful assistant",
    model=model,
    model_settings=ModelSettings(temperature=0.9, top_p=0.5),
    tools=[get_weather],
)

ms = agent.model_settings.resolve(override=ModelSettings(temperature=0.4))
print(f"agent model settings {agent.model_settings}")
print("\n\n==========\n\n")
print(f"new model settings {ms}")


# new_agent = agent.clone(name="NewAgent", tools=[])
# print(f"Agent {id(agent.tools)}")
# print("\n\n==========\n\n")
# print(f"New Agent {id(new_agent.tools)}")

# result = Runner.run_sync(agent, "write a quote about software development")

# print(result.final_output)


# temperature 0.5
# top_p = 0.5
# top_k
# cat sat on -----
# mat 40%
# chair 30%
# table 20%
# banana 10%

# a = 10
# b = a
# b = 20

# print(f"value of a is {a}")
# print(f"value of b is {b}")

# a = [1, 2]
# b = a
# b[0] = 3

# print(f"value of a is {a}")
# print(f"value of b is {b}")
