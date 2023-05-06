from pydantic import BaseModel


class HotelInfo(BaseModel):
    id: int
    name: str
    location: str
    services: str
    rooms_quantity: int
    image_id: int
