from agents import Agent
from my_config.gemini_confg import MODEL
from my_agent.my_agents import math_agent

nextjs_assistant = Agent(
    name="next js Assistant",
    instructions="You are helpful next js assistant",
    model=MODEL
      )

python_assistant = Agent(
    name="Python Assistant",
    instructions="You are helpful python assistant",
    model=MODEL
)

#  Traige Agent
sir_bilal = Agent( 
    name="Sir Bilal",
    instructions="You are helpfull assiatnt  delegate task according to given query",
    handoffs=[nextjs_assistant,python_assistant,math_agent],
    model=MODEL
)

