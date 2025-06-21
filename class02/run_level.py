from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
    RunConfig,
)
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI
import os
import asyncio

load_dotenv(find_dotenv(), override=True)
#set_tracing_disabled(True)
api_key = os.getenv("GEMINI_API_KEY")
base_path = os.getenv("GEMINI_BASE_PATH")
model_name = os.getenv("GEMINI_MODEL_NAME")

client = AsyncOpenAI(api_key=api_key, base_url=base_path)
model = OpenAIChatCompletionsModel(openai_client=client, model=str(model_name))

math_agent: Agent = Agent(
    name="Math Agent",
    instructions="""
    - You are a Math Agent and your task is to solve math problems. 
    - define your solution step by step.
    - DO NOT reply if the question is not related to math.
    - Do NOT generate answer if question are other then math problems or you can simply say I don't know about this".
    """,
)

physics_agent: Agent = Agent(
    name="Physics Agent",
    instructions="Physics Agent is a physics tutor who can solve physics problems.",
)

config = RunConfig(
    model=model,
    tracing_disabled=True
)
prompt = input("Enter your question : ")
result = Runner.run_sync(physics_agent, prompt, run_config=config)
print(result.final_output)
