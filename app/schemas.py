from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None