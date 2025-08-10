from agents import Agent
from my_config.gemini_confg import MODEL
from data_schema.myDataSchema import MyDataType

guardrial_agent = Agent(
    name="Guradrial Agent for Hotel Sannata",
    instructions="Check queries for hotel sannata",
    model=MODEL,
    output_type=MyDataType

)