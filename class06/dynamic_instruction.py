from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    OpenAIResponsesModel,
    RunContextWrapper,
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

model = OpenAIChatCompletionsModel(model=str(model_name), openai_client=client)


def dynamic_instruction(ctx: RunContextWrapper, agent: Agent):
    style = ctx.context["style"]
    if style == "haiku":
        return "Response only in haiku style"
    elif style == "pirate":
        return "Response only in pirate style"
    else:
        return "Response in robot style, add beep beep mostly in response"


agent = Agent(
    name="helpful agent",
    instructions=dynamic_instruction,
    model=model,
)


async def main():
    prompt = input("Enter your question : ")
    result = await Runner.run(agent, prompt, context={"style": "haiku"})
    print(result.final_output)


asyncio.run(main())
# user_prompt = {"content": prompt, "role": "user"}
# result = Runner.run_sync(agent, prompt)

# print(result.final_output)
