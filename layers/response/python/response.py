import json


def success(body):
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body)
    }


def error(code, message):
    return {
        'statusCode': code,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': f'{code}: {message}'
    }
