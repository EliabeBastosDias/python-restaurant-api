from typing import Type, TypeVar, Generic, Optional, List, Dict
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from internal.core.interfaces.repo_interface import IRepository

T = TypeVar("T")

ITEM_BY_PAGE = 15


class BaseRepository(IRepository[T], Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self._session = session
        self._model = model

    def insert(self, item: T) -> T:
        try:
            self._session.add(item)
            self._session.commit()
            return item
        except SQLAlchemyError as exception:
            self._session.rollback()
            raise exception
        finally:
            self._session.close()

    def get(self, token: str, onlyActives: bool = False) -> Optional[T]:
        try:
            query = self._session.query(self._model).filter_by(token=token)
            if onlyActives:
                query = query.filter_by(active=True)

            return query.first()
        except SQLAlchemyError as exception:
            raise RuntimeError(f"Database error occurred: {exception}") from exception
        finally:
            self._session.close()

    def list(self, onlyActives: bool, page: int = 1) -> List[Dict]:
        try:
            offset = (page - 1) * ITEM_BY_PAGE

            query = select(self._model)
            if onlyActives:
                query = query.filter(self._model.active is True)

            paginated_query = query.offset(offset).limit(ITEM_BY_PAGE)

            result = self._session.execute(paginated_query).scalars().all()
            return [menu.to_dict() for menu in result]
        except SQLAlchemyError as exception:
            self._session.rollback()
            raise exception
        finally:
            self._session.close()

    def update(self, item_data: dict, token: str) -> Optional[T]:
        try:
            item = self._session.query(self._model).filter_by(token=token).first()
            if item:
                for key, value in item_data.items():
                    setattr(item, key, value)
                self._session.commit()
                return item
            return None
        except SQLAlchemyError as exception:
            self._session.rollback()
            raise exception
        finally:
            self._session.close()

    def inactivate(self, token: str) -> Optional[T]:
        try:
            item = self._session.query(self._model).filter_by(token=token).first()
            if item:
                item.active = False
                self._session.commit()
                return item
            return None
        except SQLAlchemyError as exception:
            self._session.rollback()
            raise exception
        finally:
            self._session.close()

    def delete(self, token: str) -> bool:
        try:
            item = self._session.query(self._model).filter_by(token=token).first()
            if item:
                self._session.delete(item)
                self._session.commit()
                return True
            return False
        except SQLAlchemyError as exception:
            self._session.rollback()
            raise exception
        finally:
            self._session.close()
