from agents import function_tool, RunContextWrapper, FunctionTool
from tool_schema.my_tool_schema import MyToolSchema

async def subtract_function(ctx:RunContextWrapper, arg):
    print("Subtract tool fire -->")
    obj = MyToolSchema.model_validate_json(arg)
    return f"you answer is {obj.n1 -  obj.n2}" 


subtract = FunctionTool(
    name="subtract",
    description="Subtract function.",
    params_json_schema=MyToolSchema.model_json_schema(),
    on_invoke_tool=subtract_function
)

@function_tool
def plus(ctx:RunContextWrapper,n1:int,n2:int):
    """Plus function"""
    print("Plus tool fire ----->")
    print("ctx ---->",ctx.context["age"])
    return f"your answer is {n1+n2}"