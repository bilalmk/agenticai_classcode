from agents import function_tool

@function_tool
def plus(n1:int,n2:int) -> str:
    """
    simple plus funciton that return the sum of two number

    Args:
    n1 : int
    n2: int
    """
    return f"you answer is {n1+n2}"


