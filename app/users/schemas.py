import strawberry


@strawberry.input
class CreateUser:
    name: str
    age: int


@strawberry.input
class UpdateUser(CreateUser):
    id: int


@strawberry.type
class GetUser(UpdateUser):
    pass
