import strawberry
from strawberry.asgi import GraphQL


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User("Vlad", 20)


schema = strawberry.Schema(Query)
graphql_app = GraphQL(schema)

# from gql import gql, Client
# from gql.transport.aiohttp import AIOHTTPTransport
#
# # Select your transport with a defined url endpoint
# transport = AIOHTTPTransport(url="http://127.0.0.1/graphql")
#
# # Create a GraphQL client using the defined transport
# client = Client(transport=transport, fetch_schema_from_transport=True)
#
# # Provide a GraphQL query
# query = gql(
#     """
#     query Query {
#         user {
#         name
#         age
#       }
#     }
# """
# )
#
# # Execute the query on the transport
# result = client.execute(query)
# print(result)
