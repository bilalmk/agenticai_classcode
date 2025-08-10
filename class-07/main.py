from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_export_api_key
from dotenv import find_dotenv, load_dotenv
import os
import asyncio

from pydantic import BaseModel

load_dotenv(find_dotenv(), override=True)

api_key = os.getenv("OPENAI_API_KEY1")
base_url = os.getenv("OPENAI_BASE_URL1")
model_name = os.getenv("OPENAI_MODEL_NAME1")


client = AsyncOpenAI(api_key=api_key, base_url=base_url)
model = OpenAIChatCompletionsModel(openai_client=client, model=model_name)

set_tracing_export_api_key(api_key=api_key)


class CountryOutPut(BaseModel):
    country: str
    province: str
    major_cities: list[str]
    population: str

class MathOutPut(BaseModel):
    is_math:bool
    reason:str

agent = Agent(
    "GeneralAgent",
    instructions="You are a helpful agent",
    model=model,
    output_type=MathOutPut,
)


async def main():
    msg = input("Enter you question : ")
    result = await Runner.run(agent, msg)
    print(result.final_output)


asyncio.run(main())
