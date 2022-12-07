from fastapi import Depends
from app.db import get_db


def get_db_contex(db=Depends(get_db)):
    return {"db": db}
