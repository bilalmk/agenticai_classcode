from pydantic import BaseModel

class MyData(BaseModel):
    n1:int
    n2:int
    result:int