import json
import os

import boto3

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)


def find_public_notes(event, context):
    print('Find public notes')
    data = table.scan()
    notes = data['Items'] if 'Items' in data else []
    return success(notes)


def success(body):
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body)
    }
