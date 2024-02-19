import json
from pymongo import MongoClient
from bson.json_util import dumps


def get_inventario(event, context):
    uri = "mongodb+srv://sozastev:3UlUoyRsHdFJJMI8@link.k3fwk6i.mongodb.net/?retryWrites=true&w=majority"
    db = MongoClient(uri).get_database("link").get_collection("inventario")
    try:
        result = list(db.find(filter={}, projection={"_id": 0}))

        # result = dumps(result)
        # result.replace('\\', '')
        result = json.loads(result)
    except Exception as ex:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "error"
            })
        }

    body = {
        "inventario": result
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }