import json

class JsonHandler:
    def serialize_result(result):
        return json.dumps(result.to_dict())