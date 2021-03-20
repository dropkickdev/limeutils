Redis Utilities
===============

The `Red` class uses the official [redis](https://pypi.org/project/redis/) python package in
 its methods. Limeutils acts as
 a wrapper simplifying the use of the package and parsing all data it returns into valid python data
  types.

Quickstart
----------
Get yourself up and running

```python
{!examples/redis01.py!}

```

Example
-------

```python
from limeutils import Red

r = Red()

# Or set a custom config
CACHE_CONFIG = {
    'pre':  'FOOBAR',           # Defaults to ''
    'ver':  'v1',               # Defaults to ''
    'ttl':  3600 * 24 * 15,     # Defaults to -1
}
r = Red(**CACHE_CONFIG)
```

With connection information

```python
from limeutils import Red

CACHE_CONFIG = {
    'host': 'localhost',
    'port': 6379,
    'db':   0,
    'pre':  'FOOBAR',
    'ver':  'v1',
    'ttl':  3600 * 24 * 15,    
}
r = Red(**CACHE_CONFIG)
```

If you don't include any connection information then the redis defaults will be used.

Key Prefixes
-------------
Limeutils lets you use prefixes for your keys allowing for better key
 management. Just add it when you create your object.
 
```python hl_lines="1"
r = redis.Redis(pre='FOOBAR', ver='v1')
```
- `pre`: Prefix for your project. Defaults to an empty string.
- `ver`: Version for your key. Defaults to an empty string.

This makes sure you won't overrite any keys from other projects.

!!! info
    Keys are saved as **prefix:version:key** in redis (if you used the arguments `pre`, `ver`, or
     both). Creating a key named `user` in python is saved as `FOOBAR:v1:user` in redis. But when
      you need to use this key in python you only type the name `user` and the `r` object
      prepends the prefixes for you. 

<a id="api"></a>

Redis API
----------

All methods are accessible from an instance of the `Redis` class. These are all validated using
 [Pydantic](https://pydantic-docs.helpmanual.io/) models.
 
**`get(key, default='', pre=None, ver=None)`**
: Get the value of a single non-hash key. To set the value of this key use **`set()`**.

: *Returns*: `Union[str, int, float]`

: - `key`: Key name
- `default`: Use this value if key doesn't exist
{!partials/prever!}

**`hget(key, field, default='', pre=None, ver=None)`**
: Get a single field from a hash key. To set the value of this field use **`hset()`** or **`hmset()
`**.

: *Returns*: `Union[str, int, float]`

: - `key`: Key name
- `field`: Field name
- `default`: Use this value if field doesn't exist
{!partials/prever!}

**`hmget(key: str, fields=None, pre=None, ver=None)`**
: Get multiple fields from a hash key. To set the value of these fields use **`hset()`** or
 **`hmset()**.

: *Returns*: `dict`

: - `key`: Key name
- `fields`: List/Tuple of field names
{!partials/prever!}

**`hmset(key, mapping, ttl=None, pre=None, ver=None)`**
: Add multiple fields to a hash key. If the key doesn't exist it is created. Validation done by the
 pydantic model **Hmset**.
 
: *Returns*: `int` Number of fields set. Updating an existing field counts as 0 not 1.
 
: - `key`: Key name
- `mapping`: Dict of field-val pairs
{!partials/ttlprever!}

**`hset(key, field, val='', mapping=None, ttl=None, pre=None, ver=None)`**
: Add a single field to a hash key. If the key doesn't exist it is created.

: *Returns*: `int` Number of fields set. Updating an existing field counts as 0 not 1.
 
: - `key`: Key name
- `field`: Field name
- `val`: Key value
- `mapping`: Dict of field-val pairs
{!partials/ttlprever!}

**`set(key, val='', xx=False, keepttl=False, ttl=None, pre=None, ver=None)`**
: Create or update a single non-hash key. To read this key use **`get()`**.

: *Returns*: `int` Number of keys created. Updated keys aren't counted.

: - `key`: Key name
- `val`: Key value
- `xx`: Set to val only if key already exists
- `keepttl`: Retain the time to live associated with the key.
{!partials/ttlprever!}