from pydantic import BaseModel


class MenuCreateSchema(BaseModel):
    name: str


class MenuUpdateSchema(BaseModel):
    name: str
