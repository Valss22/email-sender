from fastapi import APIRouter
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

graphql_client = APIRouter()


@graphql_client.post('/graphql/client/')
def test_graphql(graphql_query: str):
    transport = AIOHTTPTransport(url="http://127.0.0.1:8000/graphql")

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    query = gql(graphql_query)
    return client.execute(query)
