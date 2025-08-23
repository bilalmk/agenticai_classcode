
import asyncio
import json
from typing import Any
from agents import (
    Agent,
    OpenAIResponsesModel,
    OpenAIChatCompletionsModel,
    Runner,
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
base_url = os.getenv("OPENAI_BASE_PATH1")
model_name = os.getenv("OPENAI_MODEL_NAME1")

set_tracing_export_api_key(str(api_key1))

client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url,
)

model = OpenAIChatCompletionsModel(model=str(model_name), openai_client=client)
config = RunConfig(model=model)