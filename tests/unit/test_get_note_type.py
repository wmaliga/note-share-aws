import json

from moto import mock_dynamodb2

from tests.unit.common.dynamodb import create_table


@mock_dynamodb2
def test_get_note_type_public():
    create_table()

    event = {
        'pathParameters': {
            'id': 'id-public'
        }
    }

    from get_note_type import app
    ret = app.get_note_type(event, {})
    body = json.loads(ret['body'])

    assert ret['statusCode'] == 200
    assert body == 'PUBLIC'


@mock_dynamodb2
def test_get_note_type_private():
    create_table()

    event = {
        'pathParameters': {
            'id': 'id-private'
        }
    }

    from get_note_type import app
    ret = app.get_note_type(event, {})
    body = json.loads(ret['body'])

    assert ret['statusCode'] == 200
    assert body == 'PRIVATE'


@mock_dynamodb2
def test_get_note_type_missing():
    create_table()

    event = {
        'pathParameters': {
            'id': 'id-missing'
        }
    }

    from get_note_type import app
    ret = app.get_note_type(event, {})

    assert ret['statusCode'] == 404
