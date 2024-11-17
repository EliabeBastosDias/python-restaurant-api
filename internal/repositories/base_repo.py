from typing import Type, TypeVar, Generic, Optional, List, Dict
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from internal.core.interfaces.repo_interface import IRepository

T = TypeVar("T")

ITEM_BY_PAGE = 15


class BaseRepository(IRepository[T], Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.__session = session
        self.__model = model

    def insert(self, item: T) -> T:
        try:
            self.__session.add(item)
            self.__session.commit()
            return item
        except SQLAlchemyError as exception:
            self.__session.rollback()
            raise exception
        finally:
            self.__session.close()

    def get(self, token: str, onlyActives: bool = False) -> Optional[T]:
        try:
            query = self.__session.query(self.__model).filter_by(token=token)
            if onlyActives:
                query = query.filter_by(active=True)

            return query.first()
        except SQLAlchemyError as exception:
            raise RuntimeError(f"Database error occurred: {exception}") from exception
        finally:
            self.__session.close()

    def list(self, onlyActives: bool, page: int = 1) -> List[Dict]:
        try:
            offset = (page - 1) * ITEM_BY_PAGE

            query = select(self.__model)
            if onlyActives:
                query = query.filter(self.__model.active is True)

            paginated_query = query.offset(offset).limit(ITEM_BY_PAGE)

            result = self.__session.execute(paginated_query).scalars().all()
            return [menu.to_dict() for menu in result]
        except SQLAlchemyError as exception:
            self.__session.rollback()
            raise exception
        finally:
            self.__session.close()

    def update(self, item_data: dict, token: str) -> Optional[T]:
        try:
            item = self.__session.query(self.__model).filter_by(token=token).first()
            if item:
                for key, value in item_data.items():
                    setattr(item, key, value)
                self.__session.commit()
                return item
            return None
        except SQLAlchemyError as exception:
            self.__session.rollback()
            raise exception
        finally:
            self.__session.close()

    def inactivate(self, token: str) -> Optional[T]:
        try:
            item = self.__session.query(self.__model).filter_by(token=token).first()
            if item:
                item.active = False
                self.__session.commit()
                return item
            return None
        except SQLAlchemyError as exception:
            self.__session.rollback()
            raise exception
        finally:
            self.__session.close()

    def delete(self, token: str) -> bool:
        try:
            item = self.__session.query(self.__model).filter_by(token=token).first()
            if item:
                self.__session.delete(item)
                self.__session.commit()
                return True
            return False
        except SQLAlchemyError as exception:
            self.__session.rollback()
            raise exception
        finally:
            self.__session.close()
