import strawberry


@strawberry.type
class UserIn:
    email: str
    password: str


@strawberry.type
class UserOut:
    id: str
    email: str
    jwt: str
