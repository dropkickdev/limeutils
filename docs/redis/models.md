# Pydantic Models

Below are some custom data types used to make the code shorter
 
<a id="custom-data-types"></a>
```python
{!examples/redis-custom-datatypes.py!}
```

The `LT` and `V` data types are used throughout this package.

Validators
----------

`nonone`
```python
def nonone(val):
    """Validator: Convert None to empty string."""
    if val is None:
        return ''
    return val
```

`nonone_mapping`
```python hl_lines="1"
def nonone_mapping(val):
    """Validator: Convert None to empty string."""
    if val is None or not val:
        return None
    else:
        for k, v in val.items():
            val[k] = '' if v is None else v
    return val
```

Models
------

`StarterModel`
```python
class StarterModel(BaseModel):
    key: V
    pre: Optional[V] = ''
    ver: Optional[V] = ''
    ttl: Optional[int] = Field(0, ge=0)
```

`Get`
```python
class Get(StarterModel):
    default: Optional[Any] = ''
```

`Hget`
```python
class Hget(StarterModel):
    default: Optional[Any] = ''
```

`Hmget`
```python
class Hmget(StarterModel):
    fields_: Optional[LT] = None
```

`Hmset`
```python
class Hmset(StarterModel):
    mapping: Optional[dict] = None
    
    _clean_mapping = validator('mapping', allow_reuse=True)(nonone_mapping)
```

`Hset`
```python
class Hset(StarterModel):
    field: str
    val: Optional[V]
    mapping: Optional[dict] = None

    _clean_val = validator('val', allow_reuse=True)(nonone)
    _clean_mapping = validator('mapping', allow_reuse=True)(nonone_mapping)
```

`Set`
```python
class Set(StarterModel):
    val: Optional[V] = ''
    xx: bool = False
    keepttl: bool = False

    _clean_val = validator('val', allow_reuse=True)(nonone)

    
    @validator('xx', 'keepttl')
    def boolonly(cls, val):
        return bool(val)
```