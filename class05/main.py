from agents import Runner, set_tracing_disabled
from my_agent.my_agents import math_agent
from my_agent.handoff_agent import sir_bilal

set_tracing_disabled(True)

# res =Runner.run_sync(starting_agent=math_agent, input="Subtract karo 100 me 50, jo answer ay us me plus 30")

# res= Runner.run_sync(starting_agent=math_agent,input="What is 2 + 5?")
# res = Runner.run_sync(
#     starting_agent=sir_bilal,
#     input="please explain middleware in next js in short")

res =Runner.run_sync(starting_agent=sir_bilal, input="Subtract karo 100 me 50, jo answer ay us me plus 30")

# print("last Agent",res.last_agent)
print("Response ",res.final_output)