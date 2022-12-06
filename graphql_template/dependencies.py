from fastapi import Depends
from graphql_template.db import get_db


def get_db_contex(db=Depends(get_db)):
    return {"db": db}
