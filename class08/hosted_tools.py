import asyncio
from typing import Any
from agents import (
    Agent,
    OpenAIChatCompletionsModel,
    OpenAIResponsesModel,
    RunContextWrapper,
    Runner,
    function_tool,
    set_tracing_export_api_key,
    RunConfig,
    WebSearchTool,
    FileSearchTool,
)

from openai import AsyncOpenAI
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(), override=True)

api_key1 = os.getenv("OPENAI_API_KEY1")
api_key = os.getenv("OPENAI_API_KEY1")
base_url = os.getenv("OPENAI_BASE_URL1")
model_name = os.getenv("OPENAI_MODEL_NAME1")

# set_tracing_disabled(True)
set_tracing_export_api_key(str(api_key1))

client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url,
)

model = OpenAIResponsesModel(model=str(model_name), openai_client=client)
config = RunConfig(model=model)

general_agent = Agent(
    "GeneralAgent",
    instructions="You are helpful assistant",
    model=model,
    tools=[
        WebSearchTool(),
        FileSearchTool(
            vector_store_ids=["you vector store id"], max_num_results=3
        ),
    ],
)


async def main():
    msg = input("Enter your query : ")
    result = await Runner.run(general_agent, msg)
    print(result.final_output)


asyncio.run(main())