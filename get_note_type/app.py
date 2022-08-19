import database
import response


def get_note_type(event, context):
    note_id = event['pathParameters']['id']
    print(f'Get note type id = {note_id}')

    note = database.get_note_type(note_id)

    if not note:
        return response.error(404, 'Note not found')

    return response.success(note['type'])
