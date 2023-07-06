from pydantic import BaseModel


class SHotelsInfo(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    rooms_quantity: int
    image_id: int


class SHotelsRoomsLeft(SHotelsInfo):
    rooms_left: int
