from typing import Type, TypeVar, Generic, Optional, List
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from internal.core.interfaces.repo_interface import IRepository
from internal.database.core_connection import DatabaseCoreConnection

T = TypeVar("T")

ITEM_BY_PAGE = 10


class BaseRepository(IRepository[T], Generic[T]):
    def __init__(self, model: Type[T]):
        self._model = model

    def insert(self, item: T) -> T:
        with DatabaseCoreConnection() as session:
            try:
                session.add(item)
                session.commit()
                session.refresh(item)
                return item
            except SQLAlchemyError as exception:
                session.rollback()
                raise exception

    def get(self, token: str, onlyActives: bool = False) -> Optional[T]:
        with DatabaseCoreConnection() as session:
            try:
                query = session.query(self._model).filter_by(token=token)
                if onlyActives:
                    query = query.filter_by(active=onlyActives)

                return query.first()
            except SQLAlchemyError as exception:
                raise exception

    def list(self, onlyActives: bool, page: int = 1) -> List[T]:
        with DatabaseCoreConnection() as session:
            try:
                offset = (page - 1) * ITEM_BY_PAGE
                query = select(self._model)

                if onlyActives is False:
                    query = query.filter(self._model.active == False)
                else:
                    query = query.filter(self._model.active == True)

                paginated_query = query.offset(offset).limit(ITEM_BY_PAGE)

                result = session.execute(paginated_query).scalars().all()
                return result
            except SQLAlchemyError as exception:
                raise exception

    def update(self, item_data: T) -> Optional[T]:
        with DatabaseCoreConnection() as session:
            try:
                session.merge(item_data)
                session.commit()
                result = (
                    session.query(self._model).filter_by(token=item_data.token).first()
                )
                return result
            except SQLAlchemyError as exception:
                session.rollback()
                raise exception

    def inactivate(self, token: str) -> None:
        with DatabaseCoreConnection() as session:
            try:
                item = session.query(self._model).filter_by(token=token).first()
                if item:
                    item.active = False
                    session.commit()
                return None
            except SQLAlchemyError as exception:
                session.rollback()
                raise exception

    def delete(self, token: str) -> bool:
        with DatabaseCoreConnection() as session:
            try:
                item = session.query(self._model).filter_by(token=token).first()
                if item:
                    session.delete(item)
                    session.commit()
                    return True
                return False
            except SQLAlchemyError as exception:
                session.rollback()
                raise exception
