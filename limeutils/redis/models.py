from typing import Optional, Union, TypeVar
from pydantic import BaseModel, Field, validator


K = TypeVar('K', str, int, float)


class StarterModel(BaseModel):
    key: str
    pre: Optional[K] = ''
    ver: Optional[K] = ''
    ttl: Optional[int] = Field(0, ge=0)


class Hset(StarterModel):
    field: str
    val: Union[str, int, float, bytes] = ''
    mapping: Optional[dict] = None
    
    
class Hmset(StarterModel):
    mapping: Optional[dict] = None

