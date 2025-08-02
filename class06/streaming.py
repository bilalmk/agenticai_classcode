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
from openai.types.responses import ResponseTextDeltaEvent
from openai import AsyncOpenAI
from dotenv import load_dotenv, find_dotenv
import os
import json

import asyncio

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

agent = Agent(name="helpful agent", instructions="You are a helpful agent", model=model)


# enable_verbose_stdout_logging()
async def main():
    print("Runner start")
    prompt = input("Enter your question : ")
    result = Runner.run_streamed(agent, prompt)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            print(event.data.delta, end="", flush=True)
            # print("\n\n============================\n\n")
    # print(result.final_output)


asyncio.run(main())
