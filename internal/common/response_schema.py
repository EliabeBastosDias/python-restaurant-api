from pydantic import BaseModel
from typing import Dict, List, Union, Generic, TypeVar


T = TypeVar("T")
class BodyModel(BaseModel, Generic[T]):
    success: bool
    message: str
    data: T


class ResponseModel(BaseModel, Generic[T]):
    status_code: int
    content: BodyModel[T]

