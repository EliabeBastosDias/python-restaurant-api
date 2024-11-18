from datetime import date, datetime
import json
from typing import Dict


class JsonHandler:
    @classmethod
    def convert_types_in_dict(result: Dict) -> Dict:
        for key, value in result.items():
            if isinstance(value, (datetime, date)):
                result[key] = value.isoformat()
            elif isinstance(value, dict):
                result[key] = JsonHandler.convert_types_in_dict(value)
            elif isinstance(value, str):
                try:
                    json_data = json.loads(value)
                    if isinstance(json_data, dict):
                        result[key] = JsonHandler.convert_types_in_dict(json_data)
                    else:
                        result[key] = json_data
                except (json.JSONDecodeError, TypeError):
                    pass
        return result

    def serialize_result(result):
        if isinstance(result, dict):
            result = JsonHandler.convert_types_in_dict(result)

        return json.dumps(result)
