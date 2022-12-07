from pydantic import BaseModel
import strawberry


@strawberry.type
class User:
    name: str
    age: int


class UserCreate(BaseModel):
    name: str
    age: int
