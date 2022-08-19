import os

import boto3

table_name = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)


def find_public_notes():
    data = table.scan()
    return data.get('Items', [])


def get_note_type(note_id):
    data = table.get_item(
        Key={'id': note_id},
        AttributesToGet=['type']
    )

    return data.get('Item', None)


def get_note(note_id):
    data = table.get_item(
        Key={'id': note_id}
    )

    return data.get('Item', None)


def save_note(note):
    table.put_item(Item=note)