from app.users.model import users
from databases import Database
from app.users.schemas import GetUser, CreateUser, UpdateUser


async def create_user(user: CreateUser, db: Database) -> None:
    user_query = users.insert().values(**user.__dict__)
    await db.execute(user_query)
    return None


async def update_user(user: UpdateUser, db: Database) -> None:
    user_query = users.update().where(users.c.id == user.id).values(**user.__dict__)
    await db.execute(user_query)
    return None


async def delete_user(id: int, db: Database) -> None:
    user_query = users.delete().where(users.c.id == id)
    await db.execute(user_query)
    return None


async def get_user_by_id(id: int, db: Database) -> GetUser:
    user_query = users.select().where(users.c.id == id)
    return await db.fetch_one(user_query)


async def get_users_list(db: Database):
    users_query = users.select()
    return await db.fetch_all(users_query)
