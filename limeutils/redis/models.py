from typing import Optional, Union, TypeVar
from pydantic import BaseModel, Field, validator


LT = Union[list, tuple]
V = Union[str, int, float, bytes]



def listmaker(val):
    """Validator: Convert str to list with one item."""
    if isinstance(val, str):
        return [val]
    return val

def nonone(val):
    """Validator: Convert None to empty string."""
    if val is None:
        return ''
    return val


class StarterModel(BaseModel):
    key: V
    pre: Optional[V] = ''
    ver: Optional[V] = ''
    ttl: Optional[int] = Field(0, ge=0)
    

class Hset(StarterModel):
    field: str
    val: Optional[V]
    mapping: Optional[dict] = None
    
    @validator('val')
    def nonetostr(cls, val):
        return nonone(val)
    
    
class Hmset(StarterModel):
    mapping: Optional[dict] = None

    @validator('mapping')
    def nonetostr(cls, val):
        return nonone(val)


class Set(StarterModel):
    val: Optional[V] = ''
    xx: bool = False
    keepttl: bool = False


    @validator('val')
    def nonetostr(cls, val):
        return nonone(val)

    
    @validator('xx', 'keepttl')
    def boolonly(cls, val):
        return bool(val)
    

class Get(StarterModel):
    pass

    
class Hmget(StarterModel):
    fields_: Optional[LT] = None


class Hdel(StarterModel):
    fields_: Optional[Union[str, LT]] = None
    
    @validator('fields_')
    def makelist(cls, val):
        return listmaker(val)
    
    
class Delete(BaseModel):
    key: Union[str, LT]
    pre: Optional[V] = ''
    ver: Optional[V] = ''

    @validator('key')
    def makelist(cls, val):
        return listmaker(val)