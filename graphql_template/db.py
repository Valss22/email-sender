import databases
import sqlalchemy


DB_URL = "sqlite:///./sql_app.db"

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DB_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)


async def get_db():
    try:
        db = databases.Database(DB_URL)
        await db.connect()
        yield db
    finally:
        await db.disconnect()
