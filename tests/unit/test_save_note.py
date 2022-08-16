import json

from moto import mock_dynamodb2

from tests.unit.common.dynamodb import create_table, note_public, note_private, note_expired


@mock_dynamodb2
def test_save_note_public():
    create_table()

    event = {
        'body': json.dumps(note_public())
    }

    from save_note import app
    ret = app.save_note(event, {})
    body = json.loads(ret['body'])

    assert ret['statusCode'] == 200
    assert len(body) == 36


@mock_dynamodb2
def test_save_note_private():
    create_table()

    event = {
        'body': json.dumps(note_private())
    }

    from save_note import app
    ret = app.save_note(event, {})
    body = json.loads(ret['body'])

    assert ret['statusCode'] == 200
    assert len(body) == 36


@mock_dynamodb2
def test_save_note_malformed():
    create_table()

    note = note_private()
    del note['type']

    event = {
        'body': json.dumps(note)
    }

    from save_note import app
    ret = app.save_note(event, {})

    assert ret['statusCode'] == 400


@mock_dynamodb2
def test_save_note_expired():
    create_table()

    event = {
        'body': json.dumps(note_expired())
    }

    from save_note import app
    ret = app.save_note(event, {})

    assert ret['statusCode'] == 422


@mock_dynamodb2
def test_save_note_no_password():
    create_table()

    note = note_private()
    del note['password']

    event = {
        'body': json.dumps(note)
    }

    from save_note import app
    ret = app.save_note(event, {})

    assert ret['statusCode'] == 422
