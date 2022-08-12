import json
import os
from datetime import datetime
from uuid import uuid4

import boto3

DATE_FORMAT = '%Y-%m-%d'

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)


def save_note(event, context):
    note = json.loads(event['body'])
    note['id'] = str(uuid4())
    print(f'Save note: {note}')

    if 'type' not in note:
        return error(400, 'Missing type')
    if 'title' not in note:
        return error(400, 'Missing title')
    if 'expirationDate' not in note:
        return error(400, 'Missing expiration date')
    if 'data' not in note:
        return error(400, 'Missing data')

    if datetime.strptime(note['expirationDate'], DATE_FORMAT) < datetime.now():
        return error(422, 'Expiration date cannot be in the past')

    if note['type'] == 'PRIVATE':
        if 'password' not in note or not note['password']:
            return error(422, 'Missing password')
    else:
        note.pop('password', None)

    table.put_item(Item=note)

    return success(note['id'])


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
