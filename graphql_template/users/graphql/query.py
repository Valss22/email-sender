import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info
from graphql_template.users.services import create_user
from graphql_template.users.schemas import UserCreate
from graphql_template.dependencies import get_db_contex


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class UserMutation:
    @strawberry.field
    async def create_user(self, info: Info) -> None:
        user = UserCreate(name="test", age=10)
        await create_user(user, info.context["db"])
        return None


schema = strawberry.Schema(UserMutation)
graphql_app = GraphQLRouter(schema, context_getter=get_db_contex)
