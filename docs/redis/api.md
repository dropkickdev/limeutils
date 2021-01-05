Redis
=====

The `Redis()` class uses the official [redis](https://pypi.org/project/redis/) python package in
 its methods. Limeutils acts as
 a wrapper parsing all data it returns into valid python data types.

Quickstart
----------
Get yourself up and running

```python hl_lines="1-2"
{!examples/redis01.py!}

```

Setup
-----

```python
from limeutils import redis

# Create the redis object
r = redis.Redis()
```

With connection information

```python
r = redis.Redis(host='localhost', port=2468, db=0)
```

If you don't include any connection information then the redis defaults will be used.

Key Prefixes
-------------
Limeutils lets you use prefixes for your keys allowing for better key
 management.
 
```python hl_lines="1"
r = redis.Redis(pre='FOOBAR', ver='v1')
```
- `pre`: Prefix for your project. Defaults to an empty string.
- `ver`: Version for your key. Defaults to an empty string.

This makes sure you won't overrite any keys from other projects.

!!! info
    Keys you create are automatically saved in the **prefix:version:key** format (if
     you used the arguments `pre`, `ver`, or both).
    Creating a key named `user` in python is saved as `FOOBAR:v1:user` in redis. But when you need
     to use this key in your python code you only type the name `user` and the `r` object
      prepends the
      prefixes for you.
      
      If you don't want to use any prefixing just don't use the `pre` and `ver` arguments when
       creating the object. This would mean your original key of `user` in pyhon would also be
        saved as `user` in redis. 

<a id="api"></a>

Redis API
----------
All methods are accessible from an instance of the `Redis` class. These are all validated using
 [Pydantic](https://pydantic-docs.helpmanual.io/) models.
 
_______________________________________________________________________
`get(key, default='', pre=None, ver=None)`
: Get the value of a single non-hash key. To set the value of this key use **`set()`**. <br>
**Returns**: `Union[str, int, float]`

: - `key`: Key name
- `default`: Use this value if key doesn't exist
- `pre`: Custom prefix. Overrides the prefix set when you created the object.
- `ver`: Custom version. Overrides the version set when you created the object.

`hget()`
: To follow

`hmget()`
: To follow

`hmset()`
: To follow

`hset(key, field, val='', mapping=None, ttl=None, pre=None, ver=None)`
: Add a single field to a hash key. If the key doesn't exist it is created. <br>
**Returns**: `int` Number of fields set. Updating an existing field counts as 0 not 1.
 
: - `key`: Key name
- `field`: Field name
- `val`: Key value. See [custom data type](#custom-data-types).
- `mapping`: Dict of field-val pairs
{!partials/ttlprever!}

`set(key, val='', xx=False, keepttl=False, ttl=None, pre=None, ver=None)`
: Create or update a single non-hash key. To read this key use **`get()`**. <br>
**Returns**: `int` Number of keys created. Updated keys aren't counted.

: - `key`: Key name
- `val`: Key value. See [custom data type](#custom-data-types).
- `xx`: Set to val only if key already exists
- `keepttl`: Retain the time to live associated with the key.
{!partials/ttlprever!}


`hget()`
