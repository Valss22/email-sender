from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
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

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.user.model"]},
    generate_schemas=False,
    add_exception_handlers=True,
)
