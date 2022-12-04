import strawberry


@strawberry.type
class UserIn:
    email: str
    name: str
