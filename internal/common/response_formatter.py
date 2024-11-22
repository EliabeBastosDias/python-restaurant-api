from typing import Dict, Union
from .response_schema import BodyModel, ResponseModel
from datetime import datetime, date
from pydantic import BaseModel
import json


class ResponseFormatter:
    def __init__(self):
        pass

    @staticmethod
    def _convert_types_in_dict(data: Dict) -> Dict:
        for key, value in data.items():
            if isinstance(value, (datetime, date)):
                data[key] = value.isoformat()
            elif isinstance(value, dict):
                data[key] = ResponseFormatter._convert_types_in_dict(value)
            elif isinstance(value, str):
                try:
                    json_data = json.loads(value)
                    if isinstance(json_data, dict):
                        data[key] = ResponseFormatter._convert_types_in_dict(json_data)
                    else:
                        data[key] = json_data
                except (json.JSONDecodeError, TypeError):
                    pass
        return data

    def format_response(
        self,
        status_code: int,
        message: str,
        data: Union[BaseModel, Dict, str],
        error: bool = False,
    ) -> ResponseModel:
        if isinstance(data, BaseModel):
            data = data.model_dump()
        if isinstance(data, dict):
            data = self._convert_types_in_dict(data)

        content = BodyModel(success=not error, message=message, data=data)
        response = ResponseModel(status_code=status_code, content=content)
        return response
