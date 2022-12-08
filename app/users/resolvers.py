import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info
from app.users import services
from app.dependencies import get_db_contex
from app.users.schemas import CreateUser, UpdateUser, GetUser


@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def create_user(self, user: CreateUser, info: Info) -> None:
        await services.create_user(user, info.context["db"])

    @strawberry.mutation
    async def update_user(self, user: UpdateUser, info: Info) -> None:
        await services.update_user(user, info.context["db"])

    @strawberry.mutation
    async def delete_user(self, id: int, info: Info) -> None:
        await services.delete_user(id, info.context["db"])


@strawberry.type
class UserQuery:
    @strawberry.field
    async def get_user_by_id(self, id: int, info: Info) -> GetUser:
        return await services.get_user_by_id(id, info.context["db"])

    @strawberry.field
    async def get_users_list(self, info: Info) -> list[GetUser]:
        return await services.get_users_list(info.context["db"])


user_schema = strawberry.Schema(UserQuery, UserMutation)
user_graphql_router = GraphQLRouter(user_schema, context_getter=get_db_contex)
