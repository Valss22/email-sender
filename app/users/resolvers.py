import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info
from app.users import services
from app.dependencies import get_db_contex
from app.users.schemas import CreateUserIn, UpdateUserIn, UserOut


@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def create_user(self, user: CreateUserIn, info: Info) -> None:
        await services.create_user(user, info.context["db"])

    @strawberry.mutation
    async def update_user(self, user: UpdateUserIn, info: Info) -> None:
        await services.update_user(user, info.context["db"])


@strawberry.type
class UserQuery:
    @strawberry.field
    async def get_user_by_id(self, id: int, info: Info) -> UserOut:
        return await services.get_user_by_id(id, info.context["db"])

    @strawberry.field
    async def get_users_list(self, info: Info) -> list[UserOut]:
        return await services.get_users_list(info.context["db"])


user_schema = strawberry.Schema(UserQuery, UserMutation)
user_graphql_router = GraphQLRouter(user_schema, context_getter=get_db_contex)
