from agents import Agent, OpenAIChatCompletionsModel, Runner
from openai import AsyncOpenAI
from decouple import config


SECRET_KEY = config('GEMINI_API_KEY')

client = AsyncOpenAI(
    api_key=SECRET_KEY ,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)

math_agent = Agent(name="math teacher", instructions="you are a math teacher.", model=model) 
emg_agent = Agent(name="english teacher", instructions="you are a math teacher.", model=model) 

result = Runner.run_sync(math_agent, "plus 10 in 1000" )

print(result.final_output)



# response = client.chat.completions.create(
#     model="gemini-2.0-flash",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Explain to me how AI works"
#         }
#     ]
# )

# print(response.choices[0].message)