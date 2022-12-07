from app.users.model import users
from app.users.schemas import UserCreate
from databases import Database


async def create_user(user, db: Database) -> None:
    print(user)
    # user_query = users.insert().values(name=name, age=age)
    # await db.execute(user_query)
    return None


async def get_users_list(db: Database):
    users_query = users.select()
    return await db.fetch_all(users_query)
