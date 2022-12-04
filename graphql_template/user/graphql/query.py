import strawberry
from strawberry.asgi import GraphQL


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User("Vlad", 20)


schema = strawberry.Schema(Query)
graphql_app = GraphQL(schema)
