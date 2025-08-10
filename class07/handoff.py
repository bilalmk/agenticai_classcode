from typing import Any
from openai import AsyncOpenAI
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrail,
    RunContextWrapper,
    Runner,
    OpenAIChatCompletionsModel,
    OpenAIResponsesModel,
    TResponseInputItem,
    input_guardrail,
    set_tracing_export_api_key,
    InputGuardrailTripwireTriggered,
    enable_verbose_stdout_logging,
    trace
)
from dotenv import find_dotenv, load_dotenv
import os
import asyncio

from pydantic import BaseModel

load_dotenv(find_dotenv(), override=True)

api_key = os.getenv("OPENAI_API_KEY1")
base_url = os.getenv("OPENAI_BASE_URL1")
model_name = os.getenv("OPENAI_MODEL_NAME1")


client = AsyncOpenAI(api_key=api_key, base_url=base_url)
model = OpenAIResponsesModel(openai_client=client, model=str(model_name))

set_tracing_export_api_key(api_key=str(api_key))

math_agent = Agent(
    "MathAgent",
    instructions="You are a Math Agent, solve only math related queries",
    handoff_description="Solve math questions",
    model=model
)

physics_agent = Agent(
    "PhysicsAgent",
    instructions="You are a Physics Agent, solve only Physics related queries",
    handoff_description="Solve Physics questions",
    model=model
)

triage_agent = Agent(
    "TriageAgent",
    instructions="""
     - You are a triage agent
     - Hand off to math agent if input is related to math
     - Hand off ot physics agent if input is related to physics
     """,
    handoffs=[math_agent, physics_agent],
    model=model
)

async def main():
    with trace(workflow_name="Custom Handoff"):
        msg = input("Enter your question : ")
        result = await Runner.run(triage_agent, msg)
        print(result.final_output)
    
asyncio.run(main())