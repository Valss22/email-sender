from app.users.model import users
from databases import Database
from app.users.schemas import UserOut


async def create_user(user, db: Database) -> None:
    user_query = users.insert().values(name=user.name, age=user.age)
    await db.execute(user_query)
    return None


async def get_user_by_id(id: int, db: Database) -> UserOut:
    user_query = users.select().where(users.c.id == id)
    return await db.fetch_one(user_query)


async def get_users_list(db: Database):
    users_query = users.select()
    return await db.fetch_all(users_query)
