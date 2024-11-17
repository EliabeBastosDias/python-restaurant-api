from dataclasses import dataclass


@dataclass
class CreateMenuParams:
    name: str


@dataclass
class UpdateMenuParams:
    name: str


@dataclass
class GetParams:
    token: str


@dataclass
class InactivateMenuParams:
    token: str


@dataclass
class ListMenuParams:
    onlyActives: bool
    page: int
