from typing import Union, List, Optional
from pydantic import BaseModel, AnyHttpUrl, conint


class ActiveSchema(BaseModel):
    active: bool


class StatusSchema(BaseModel):
    status: int
