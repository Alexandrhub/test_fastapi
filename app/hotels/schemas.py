from pydantic import BaseModel, Json


class HotelInfo(BaseModel):
    id: int
    name: str
    location: str
    services: str
    rooms_quantity: int
    image_id: int