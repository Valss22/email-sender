from graphql_template.users.model import users
from graphql_template.users.schemas import UserCreate
from databases import Database
from graphql_template.utils import nonblock


async def create_user(user: UserCreate, db: Database) -> None:
    user_query = users.insert().values(name=user.name)
    nonblock(db.execute, user_query)
    return None


async def get_users_list(db: Database):
    users_query = users.select()
    return await db.fetch_all(users_query)
