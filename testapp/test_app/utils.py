import json
def is_json(data):
    try:
        json_P=json.loads(data)
        valid=True
    except ValueError:
        valid=False
    return valid