# from my_data_type.my_type import MyUserData
from pydantic import BaseModel

class MyUserData(BaseModel):
    name:str
    age:int
    email:str

user1 = MyUserData(name="Sir aneeq", age=40, email="bilal@researchcollective.org")
