import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info
from app.users.services import create_user, get_users_list
from app.users.schemas import UserCreate
from app.dependencies import get_db_contex
from app.users.schemas import User


@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def create_user(self, info: Info) -> None:
        user = UserCreate(name="test", age=10)
        await create_user(user, info.context["db"])
        return None


@strawberry.type
class UserQuery:
    @strawberry.field
    async def get_users_list(self, info: Info) -> list[User]:
        return await get_users_list(info.context["db"])


user_schema = strawberry.Schema(UserQuery, UserMutation)
user_graphql_router = GraphQLRouter(user_schema, context_getter=get_db_contex)
