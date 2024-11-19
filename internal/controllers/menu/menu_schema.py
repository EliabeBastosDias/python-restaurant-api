from dataclasses import dataclass
from datetime import datetime
from os import name
import token
from typing import Optional
from pydantic import BaseModel

class MenuRequestDTO(BaseModel):
    name: str

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
    


# @dataclass
# class MenuRequestDTO:
#     name: str
# @dataclass
# class MenuResponseDTO:
#     token: str
#     name: str
#     active: bool
#     created_at: datetime
#     updated_at: Optional[datetime]

# @dataclass
# class ListMenuRequestDTO:
#     onlyActives: bool
#     page: int

# @dataclass
# class GetMenuRequestDTO:
#     token: str

# @dataclass
# class InactivateMenuRequestDTO:
#     token: str


