from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .users.graphql.query import graphql_app

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(graphql_app, prefix="/graphql")
app.add_websocket_route("/graphql", graphql_app)
