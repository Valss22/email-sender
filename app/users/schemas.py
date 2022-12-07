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
