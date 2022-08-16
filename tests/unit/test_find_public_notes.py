import json

from moto import mock_dynamodb2

from tests.unit.common.dynamodb import create_table


@mock_dynamodb2
def test_find_public_notes():
    create_table()

    from find_public_notes import app
    ret = app.find_public_notes({}, {})
    body = json.loads(ret['body'])

    assert ret['statusCode'] == 200
    assert len(body) == 3
