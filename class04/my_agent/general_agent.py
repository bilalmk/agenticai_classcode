from agents import Agent, function_tool, RunContextWrapper
from my_config.gemini_confg import MODEL
from my_user_data.my_user import MyUserData

@function_tool
def plus(ctx:RunContextWrapper,n1,n2):
    print("Plus tool fire ---->")
    print(ctx.context)
    return f"{n1+n2}"

@function_tool
def user_age(abc:RunContextWrapper[MyUserData]):
    print("User age fire ---->")
    return f" user age is {abc.context.age}"

def dynamic_instruction(ctx:RunContextWrapper[MyUserData],agent:Agent[MyUserData]):
    return f"The user's name is {ctx.context.name}. you are helpful math teacher."


general_agent = Agent[MyUserData](
    name="MAth Teacher", 
    instructions=dynamic_instruction,
    model=MODEL,
    tools=[plus,user_age]
    
    )
