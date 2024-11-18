from dataclasses import dataclass
from typing import Dict, List, Union


@dataclass
class BodyModel:
    success: bool
    message: str
    data: Union[Dict, List[Dict], str]


@dataclass
class ResponseModel:
    status_code: int
    content: BodyModel
