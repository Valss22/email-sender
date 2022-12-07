import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info
from app.users import services
from app.dependencies import get_db_contex
from app.users.schemas import UserIn, UserOut


@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def create_user(self, user: UserIn, info: Info) -> None:
        await services.create_user(user, info.context["db"])
        return None


@strawberry.type
class UserQuery:
    @strawberry.field
    async def get_users_list(self, info: Info) -> list[UserOut]:
        return await services.get_users_list(info.context["db"])


user_schema = strawberry.Schema(UserQuery, UserMutation)
user_graphql_router = GraphQLRouter(user_schema, context_getter=get_db_contex)
