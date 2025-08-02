from agents import Agent, handoff, RunContextWrapper, function_tool
from my_config.gemini_confg import MODEL
from my_agent.my_agents import math_agent
from my_user_data.my_user import MyUserData
from pydantic import BaseModel
from agents.extensions import handoff_filters


class PythonSummary(BaseModel):
    summary: str

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

async def handoff_function(
        context:RunContextWrapper[MyUserData],
        input_data: PythonSummary
        ):
    # print("context>>>",context)
    print("input_data>>>",input_data)

    

# Agent name -> Python Assistant -> transfer_to_python_assistant
python_handoff = handoff(agent=python_assistant,
                         tool_name_override="handover_to_pyton_agent",
                        #  on_handoff=handoff_function,
                        #  input_type=PythonSummary
                        input_filter=handoff_filters.remove_all_tools
                         )

@function_tool
async def fetch_weather(city: str):
    return f"the weather in {city} is sunny 45C"


#  Traige Agent
sir_bilal = Agent( 
    name="Sir Bilal",
    instructions="You are helpfull assiatnt  delegate task according to given query",
    tools=[fetch_weather],
    handoffs=[nextjs_assistant,
              python_handoff,
            
              ],
    model=MODEL,

)

