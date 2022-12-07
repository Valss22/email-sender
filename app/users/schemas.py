from pydantic import BaseModel
import strawberry


@strawberry.input
class UserIn:
    name: str
    age: int


@strawberry.type
class UserOut:
    id: int
    name: str
    age: int


class UserCreate(BaseModel):
    name: str
    age: int
