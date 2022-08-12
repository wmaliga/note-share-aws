import json
import os
from datetime import datetime

import boto3

DATE_FORMAT = '%Y-%m-%d'

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)


def get_note(event, context):
    note_id = event['pathParameters']['id']
    password = event['headers'].get('Authorization', '')
    print(f'Get note type id = {note_id}')

    data = table.get_item(
        Key={'id': note_id}
    )

    if 'Item' not in data:
        return error(404, 'Note not found')

    note = data['Item']

    if datetime.strptime(note['expirationDate'], DATE_FORMAT) < datetime.now():
        return error(410, 'Note expired')

    if note['type'] == 'PRIVATE' and password != note['password']:
        return error(401, 'Unauthorized')

    return success(note)


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
