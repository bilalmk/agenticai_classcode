from agents import Runner, set_tracing_disabled,InputGuardrailTripwireTriggered
from my_agent.hotel_assistant import hotel_assistant

set_tracing_disabled(True)

try:

    res = Runner.run_sync(
        starting_agent=hotel_assistant, 
        input="How manay rooms available in Hotel ?",
    )

    print(res.final_output)
except InputGuardrailTripwireTriggered as e:
    print(e)