from db.base_class import Base
from db.session import engine
from .vod_rules import VodRules

__all__ = ['VodRules']

Base.metadata.create_all(engine)
