from pydantic import BaseModel

class UserCreateModel(BaseModel):
    username: str
    email: str
    password: str

class UserResponseModel(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True
