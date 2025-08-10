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
    trace,
    AgentHooks,
    
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


class MyAgentHooks(AgentHooks):
    def __init__(self):
        self.count = 0

    async def on_start(self, context: RunContextWrapper, agent: Agent) -> None:
        """Called before the agent is invoked. Called each time the running agent is changed to this
        agent."""
        self.count = 10
        print(f"\n\n agent start : {agent.name}")

    async def on_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        output: Any,
    ) -> None:
        """Called when the agent produces a final output."""
        print(f"\n\n count : {self.count}")
        print(f"\n\n agent end : {agent.name}")
        print(f"\n\n agent output : {output}")


agent = Agent(
    "GeneralAgent",
    instructions="You are a helpful agent",
    model=model,
    hooks=MyAgentHooks()
)


async def main():
    msg = input("Enter your query : ")
    result = await Runner.run(agent, msg)
    print(f"Final output : {result.final_output}")


asyncio.run(main())
