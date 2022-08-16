import os

import boto3

table_name = 'NotesTable'


def note_public():
    return {
        'id': 'id-public',
        'title': 'Public note',
        'type': 'PUBLIC',
        'expirationDate': '2030-06-08',
        'data': 'Note data'
    }


def note_private():
    return {
        'id': 'id-private',
        'title': 'Private note',
        'type': 'PRIVATE',
        'expirationDate': '2030-06-08',
        'data': 'Note data',
        'password': 'pass'
    }


def note_expired():
    return {
        'id': 'id-expired',
        'title': 'Expired note',
        'type': 'Public',
        'expirationDate': '2000-06-08',
        'data': 'Note data'
    }


def create_table():
    os.environ['TABLE_NAME'] = table_name

    dynamodb = boto3.resource('dynamodb')
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    table = dynamodb.Table(table_name)

    table.put_item(Item=note_public())
    table.put_item(Item=note_private())
    table.put_item(Item=note_expired())
