from pydantic import BaseModel
from typing import Optional, Generic, TypeVar


T = TypeVar("T")


class BodyModel(BaseModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T] = None


class ResponseModel(BaseModel, Generic[T]):
    status_code: int
    content: BodyModel[T]
