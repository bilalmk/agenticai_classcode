from agents import function_tool

@function_tool
def plus(n1:int,n2:int)->str:
    """Plus function"""
    print("Plus tool fire ---->")
    # return f"your answer in {n1+n2}"
    return n1 + n2

@function_tool
def subtract(n1:int,n2:int)->str:
    print("Subtract tool fire ---->")
    """Subtract function"""
    return f"your answer in {n1-n2}"

@function_tool
def multiply(n1:int,n2:int)->str:
    """Multiply function"""
    print("Multiply tool fire ---->")
    return f"your answer in {n1*n2}"