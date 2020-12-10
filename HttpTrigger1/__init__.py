import logging
import azure.functions as func
import requests
from azure.cosmos import CosmosClient, PartitionKey

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    digits = requests.get("https://usernameservices123.azurewebsites.net/api/HttpTrigger2").text
    letters = requests.get("https://usernameservices123.azurewebsites.net/api/HttpTrigger3").text
    username = digits + letters
    endpoint = "https://usernameservices123.documents.azure.com:443/"
    key = "fpgzmRBt4g0GqOwnUe1GY9L4qzuJ3yuLRzdaActcaSA1fIUJkVUw7f1JTA5eMTgTQ4oQ6sLCtLI4Zd57wOe3Ew=="
    client = CosmosClient(endpoint, key)

    database_name = "Usernames"
    database=client.create_database_if_not_exists(id=database_name)

    container_name = "UsernameContainer"
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/username"),
        offer_throughput=400
    )
    username_to_add = {
        "id": username
    }
    container.create_item(body=username_to_add)
    return username