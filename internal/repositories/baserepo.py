from typing import Type, TypeVar, Generic, Optional, List, Dict
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

T = TypeVar("T")

ITEM_BY_PAGE = 15

class BaseRepository(Generic[T]):
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

    def get(self, token: str, onlyActives: bool = False) -> Optional[T]:
        try:
            query = self.__session.query(self.__model).filter_by(token=token)
            if onlyActives:
                query = query.filter_by(active=True)

            return query.first()
        except SQLAlchemyError as exception:
            raise RuntimeError(f"Database error occurred: {exception}") from exception


    def list(self, onlyActives: bool, page: int = 1) -> List[Dict]:
        offset = (page - 1) * ITEM_BY_PAGE

        query = select(T) 
        if onlyActives:
            query = query.filter(T.active == True)

        paginated_query = query.offset(offset).limit(ITEM_BY_PAGE)
        
        result = self.db_session.execute(paginated_query).scalars().all()
        return [menu.to_dict() for menu in result]

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
