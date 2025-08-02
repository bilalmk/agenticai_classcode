from agents import Runner, set_tracing_disabled
from my_agent.general_agent import general_agent
from my_user_data.my_user import user1
from my_agent.handoff_agent import sir_bilal

set_tracing_disabled(True)

# res =Runner.run_sync(
#     starting_agent=general_agent, 
#     input="hi",
#     context=user1
#     )
res= Runner.run_sync(
    sir_bilal,
    "what is weather in karachi and what is python?",
    context=user1
    )

# print("Last Agent ", res.last_agent)
print("Response ",res.final_output)