import json
from datetime import datetime
from uuid import uuid4

import database
import response

DATE_FORMAT = '%Y-%m-%d'


def save_note(event, context):
    note = json.loads(event['body'])
    note['id'] = str(uuid4())
    print(f'Save note: {note}')

    if 'type' not in note:
        return response.error(400, 'Missing type')
    if 'title' not in note:
        return response.error(400, 'Missing title')
    if 'expirationDate' not in note:
        return response.error(400, 'Missing expiration date')
    if 'data' not in note:
        return response.error(400, 'Missing data')

    if datetime.strptime(note['expirationDate'], DATE_FORMAT) < datetime.now():
        return response.error(422, 'Expiration date cannot be in the past')

    if note['type'] == 'PRIVATE':
        if 'password' not in note or not note['password']:
            return response.error(422, 'Missing password')
    else:
        note.pop('password', None)

    database.save_note(note)

    return response.success(note['id'])
