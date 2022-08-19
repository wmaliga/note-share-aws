import database
import response


def find_public_notes(event, context):
    print('Find public notes')
    notes = database.find_public_notes()
    return response.success(notes)
