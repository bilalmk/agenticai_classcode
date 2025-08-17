import asyncio
import json
from typing import Any
from agents import (
    Agent,
    FunctionToolResult,
    ModelSettings,
    OpenAIResponsesModel,
    RunContextWrapper,
    Runner,
    StopAtTools,
    ToolsToFinalOutputResult,
    default_tool_error_function,
    function_tool,
    set_tracing_export_api_key,
    RunConfig,
)

from openai import AsyncOpenAI
from dotenv import load_dotenv, find_dotenv
import os

from pydantic import BaseModel

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


def custom_tool_error_function(ctx: RunContextWrapper[Any], error: Exception) -> str:
    return json.dumps({"error": True, "message": str(error)})
    # return f"custom error handle. Error: {str(error)}"


async def stop_at_tool(
    ctx: RunContextWrapper, tool_result: list[FunctionToolResult]
) -> ToolsToFinalOutputResult:
    final_output = json.loads(tool_result[0].output)
    #print(f"tool result : {tool_result}")
    
    if final_output['error']:
        return ToolsToFinalOutputResult(
            is_final_output=True, final_output=final_output['message']
        )
    else:
        return ToolsToFinalOutputResult(
            is_final_output=False, final_output=tool_result[0].output
        )


class User(BaseModel):
    user_role: str  # admin, user, student


def enable_weather_tool(ctx: RunContextWrapper[User], agent: Agent[User]) -> bool:
    if ctx.context.user_role == "admin":
        return True
    return False


@function_tool(
    name_override="get_city_weather",
    description_override="get the weather of city",
    is_enabled=enable_weather_tool,
)
def get_weather(city: str):
    "return the weather of provided city"
    print("Call tool get_weather")
    return f"{city}:35 degree"


@function_tool(failure_error_function=custom_tool_error_function)
def sum(a: int, b: int):
    "return the sum of provided numbers"
    print("Call tool sum")
    y = 10 / 0
    x = json.dumps({"error":False,'message':a+b})
    return x


general_agent = Agent[User](
    "GeneralAgent",
    instructions="You are helpful assistant",
    model=model,
    tools=[get_weather, sum],
    # model_settings=ModelSettings(tool_choice="required"),
    # reset_tool_choice=False
    tool_use_behavior=stop_at_tool,
)


async def main():
    user = User(user_role="student")
    msg = input("Enter your query : ")
    result = await Runner.run(general_agent, msg, context=user)
    print(result.final_output)
    # print(general_agent.tools[0])
    # print(sum(2,3))


asyncio.run(main())
