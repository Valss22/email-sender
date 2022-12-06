from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .users.graphql.query import user_graphql_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_graphql_router, prefix="/graphql")
app.add_websocket_route("/graphql", user_graphql_router)
