from agents import RunContextWrapper

def dynamic_instruction(ctx:RunContextWrapper,agent):
    
    return f"user name {ctx.context["name"]}, you are a helpful assistant"