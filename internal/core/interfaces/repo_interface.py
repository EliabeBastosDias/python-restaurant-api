from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, List, Dict

T = TypeVar("T")


class IRepository(ABC, Generic[T]):
    @abstractmethod
    def insert(self, item: T) -> T:
        pass

    @abstractmethod
    def get(self, token: str, onlyActives: bool = False) -> Optional[T]:
        pass

    @abstractmethod
    def list(self, onlyActives: bool, page: int = 1) -> List[Dict]:
        pass

    @abstractmethod
    def update(self, item_data: dict, token: str) -> Optional[T]:
        pass

    @abstractmethod
    def inactivate(self, token: str) -> Optional[T]:
        pass

    @abstractmethod
    def delete(self, token: str) -> bool:
        pass
