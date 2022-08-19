from datetime import datetime

import database
import response

DATE_FORMAT = '%Y-%m-%d'


def get_note(event, context):
    note_id = event['pathParameters']['id']
    password = event['headers'].get('Authorization', '')
    print(f'Get note type id = {note_id}')

    note = database.get_note(note_id)

    if not note:
        return response.error(404, 'Note not found')

    if datetime.strptime(note['expirationDate'], DATE_FORMAT) < datetime.now():
        return response.error(410, 'Note expired')

    if note['type'] == 'PRIVATE' and password != note['password']:
        return response.error(401, 'Unauthorized')

    return response.success(note)
