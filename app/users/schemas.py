import strawberry


@strawberry.input
class CreateUserIn:
    name: str
    age: int


@strawberry.input
class UpdateUserIn(CreateUserIn):
    id: int


@strawberry.type
class UserOut:
    id: int
    name: str
    age: int
