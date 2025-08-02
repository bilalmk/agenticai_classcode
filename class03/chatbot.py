import chainlit as cl
from agents import Runner
from my_agent.teacher_agent import assistant_agent

@cl.on_message
async def main(msg: cl.Message):
    prompt = msg.content
    
    res = Runner.run_sync(assistant_agent, input=prompt) 


    await cl.Message(content=f"Ai reply: {res.final_output} ").send()






# @cl.on_message
# async def main(message: cl.Message):
    
#     await cl.Message(
#         content=f"Received: {message.content}",
#     ).send()