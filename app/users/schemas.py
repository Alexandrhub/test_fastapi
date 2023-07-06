from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class SUsers(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
