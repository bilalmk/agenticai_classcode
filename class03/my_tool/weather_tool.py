from agents import function_tool

@function_tool
def fetch_weather(city: str):
    """
    fetch weather data according to given city

    Args:
    city : str
    """
    return f"sunny"
