from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class MenuRequestDTO(BaseModel):
    name: str


class CreateMenuResponseDTO(BaseModel):
    token: str


class MenuResponseDTO(BaseModel):
    token: str
    name: str
    active: bool
    created_at: datetime
    updated_at: Optional[datetime]


class ListMenuRequestDTO(BaseModel):
    onlyActives: bool
    page: int


class GetMenuRequestDTO(BaseModel):
    token: str


class InactivateMenuRequestDTO(BaseModel):
    token: str
