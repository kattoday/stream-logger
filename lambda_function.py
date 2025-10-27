import json

def lambda_handler(event, context):
    for record in event['Records']:
        print("Stream record:", json.dumps(record, indent=2))
    return {"statusCode": 200}
