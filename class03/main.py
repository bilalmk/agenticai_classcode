from my_agent.teacher_agent import math_agent, assistant_agent
from agents import Runner, enable_verbose_stdout_logging
# enable_verbose_stdout_logging()




res = Runner.run_sync(starting_agent=assistant_agent, input="please plus 2 by 2 by calling math tool")

print(res.final_output)