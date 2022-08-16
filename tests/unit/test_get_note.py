import json

from moto import mock_dynamodb2

from tests.unit.common.dynamodb import create_table


@mock_dynamodb2
def test_get_note_public():
    create_table()

    event = {
        'headers': {},
        'pathParameters': {
            'id': 'id-public'
        }
    }

    from get_note import app
    ret = app.get_note(event, {})
    body = json.loads(ret['body'])

    assert ret['statusCode'] == 200
    assert body['id'] == 'id-public'


@mock_dynamodb2
def test_get_note_private():
    create_table()

    event = {
        'headers': {
            'Authorization': 'pass'
        },
        'pathParameters': {
            'id': 'id-private'
        }
    }

    from get_note import app
    ret = app.get_note(event, {})
    body = json.loads(ret['body'])

    assert ret['statusCode'] == 200
    assert body['id'] == 'id-private'


@mock_dynamodb2
def test_get_note_missing():
    create_table()

    event = {
        'headers': {},
        'pathParameters': {
            'id': 'id-missing'
        }
    }

    from get_note import app
    ret = app.get_note(event, {})

    assert ret['statusCode'] == 404


@mock_dynamodb2
def test_get_note_expired():
    create_table()

    event = {
        'headers': {},
        'pathParameters': {
            'id': 'id-expired'
        }
    }

    from get_note import app
    ret = app.get_note(event, {})

    assert ret['statusCode'] == 410


@mock_dynamodb2
def test_get_note_unauthorized():
    create_table()

    event = {
        'headers': {
            'password': 'incorrect'
        },
        'pathParameters': {
            'id': 'id-private'
        }
    }

    from get_note import app
    ret = app.get_note(event, {})

    assert ret['statusCode'] == 401
