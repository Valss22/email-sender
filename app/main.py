# type: ignore
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
import subprocess
import sys
import uvicorn

from app.graphql_client.route import graphql_client
from app.user.graphql.query import graphql_app

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(graphql_client)
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.user.model"]},
    generate_schemas=False,
    add_exception_handlers=True,
)

if __name__ == '__main__':
    # status_output: tuple[int, str] = subprocess.getstatusoutput("mypy .")
    # if status_output[0]:
    #     print(status_output[1])
    # else:
    uvicorn.run(app, host="127.0.0.1", port=8000)
