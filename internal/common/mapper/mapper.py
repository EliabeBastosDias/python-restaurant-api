from typing import Type, TypeVar

P = TypeVar("P")
S = TypeVar("S")


class AutoMapper:
    @staticmethod
    def automapping_pydantic_to_sqlalchemy(
        pydantic_model: P, sqlalchemy_model_class: Type[S]
    ) -> S:
        if hasattr(pydantic_model, "model_dump"):
            pydantic_data = pydantic_model.model_dump()
        sqlalchemy_instance = sqlalchemy_model_class()
        for key, value in pydantic_data.items():
            if hasattr(sqlalchemy_instance, key):
                setattr(sqlalchemy_instance, key, value)
        return sqlalchemy_instance

    @staticmethod
    def automapping_sqlalchemy_to_pydantic(
        sqlalchemy_obj: S, pydantic_model_class: Type[P]
    ) -> P:
        sqlalchemy_data = {
            attr.key: getattr(sqlalchemy_obj, attr.key)
            for attr in sqlalchemy_obj.__mapper__.attrs
        }
        return pydantic_model_class(**sqlalchemy_data)


mapper = AutoMapper()
