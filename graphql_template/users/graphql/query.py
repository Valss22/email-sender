import strawberry
from strawberry.asgi import GraphQL
from graphql_template.users.services import create_user
from graphql_template.users.schemas import UserCreate
from graphql_template.db import get_db


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class UserMutation:
    @strawberry.field
    async def create_user(self) -> None:
        pass


schema = strawberry.Schema(UserMutation)
graphql_app = GraphQL(schema)
