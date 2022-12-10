import strawberry
from typing import Optional


@strawberry.input
class CreateUser:
    name: str
    age: int


@strawberry.input
class UpdateUser:
    id: int
    name: Optional[str] = None
    age: Optional[int] = None


@strawberry.type
class User(CreateUser):
    id: int
