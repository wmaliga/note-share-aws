import json
import os

import boto3

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)


def get_note_type(event, context):
    note_id = event['pathParameters']['id']
    print(f'Get note type id = {note_id}')

    data = table.get_item(
        Key={'id': note_id},
        AttributesToGet=['type']
    )

    if 'Item' not in data:
        return error(404, 'Note not found')

    return success(data['Item']['type'])


def success(body):
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body)
    }


def error(code, message):
    return {
        'statusCode': code,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': f'{code}: {message}'
    }
