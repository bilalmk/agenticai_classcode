from pydantic import BaseModel

class MyDataType(BaseModel):
    is_query_about_hotel_sannata: bool
    reason: str