# agent level configuration
# run level configuration
# global level configuration

from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI
import os
import asyncio

load_dotenv(find_dotenv(), override=True)
# set_tracing_disabled(True)
api_key = os.getenv("GEMINI_API_KEY")
base_path = os.getenv("GEMINI_BASE_PATH")
model_name = os.getenv("GEMINI_MODEL_NAME")

client = AsyncOpenAI(api_key=api_key, base_url=base_path)
model = OpenAIChatCompletionsModel(openai_client=client, model=str(model_name))
agent: Agent = Agent(
    name="GIAIC Agent", instructions="You are a helpful Math assistant", model=model
)

prompt = input("Enter your question: ")
result = Runner.run_sync(agent, prompt)
print(result.final_output)
