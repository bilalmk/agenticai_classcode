from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    OpenAIResponsesModel,
    Runner,
    set_tracing_export_api_key,
    set_tracing_disabled,
    function_tool,
    enable_verbose_stdout_logging,
)
from openai import AsyncOpenAI
from dotenv import load_dotenv, find_dotenv
import os
import json

import asyncio

import requests

load_dotenv(find_dotenv(), override=True)

api_key = os.getenv("OPENAI_API_KEY1")
base_url = os.getenv("OPENAI_BASE_URL1")
model_name = os.getenv("OPENAI_MODEL_NAME1")

# openapi_key = os.getenv("OPENAI_API_KEY1")

# set_tracing_disabled(True)
set_tracing_export_api_key(str(api_key))

client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url,
)


@function_tool
def get_weather(city: str):
    """get the weather of provided city"""
    url = f"https://api.weatherapi.com/v1/current.json?q={city}&key=1f75e21f70c34867a2392301240309"
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return "invalid response"


model = OpenAIChatCompletionsModel(model=str(model_name), openai_client=client)

agent = Agent(
    name="helpful agent",
    instructions="You are a helpful agent",
    model=model,
    tools=[get_weather],
)

# enable_verbose_stdout_logging()


async def main():
    prompt = input("Enter your question : ")
    result = await Runner.run(agent, prompt)
    print(result.final_output)


asyncio.run(main())
# user_prompt = {"content": prompt, "role": "user"}
# result = Runner.run_sync(agent, prompt)

# print(result.final_output)
