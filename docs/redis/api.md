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

Usage Example
-------------

```python
from limeutils import Red

r = Red()

# Or set your custom config
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

All methods are accessible from an instance of the `Red` class.
 
**`get(key, **kwargs)`**
: Get the value of a key. To set the value of this key use **`set()`**.
: *Returns*: Can be `string`, `int`, `float`, `byte`, `dict`, `list`, or `set`.

: - `key`: Key name
- `kwargs`: Choose from any of the custom keys below.
    - [`start=0`]: Starting index for lists
    - [`end=-1`]: Ending index for lists
    - [`only=`]: For hashes only return the fields you need

**`set(key, val, **kwargs)`**
: Create or update a new key. To read this key use **`get()`**.
: *Returns*: Varied depending on the value you set.

: - `key`: Key name
- `kwargs`: Custom keys set below. Accepts all other keys set in the parent redis package.
    - `val`: Can be `string`, `int`, `float`, `byte`, `dict`, `list`, or `set`
    - [`clear=False`]: Delete the key first instead of updating it (if `dict` or `list`)
    - [`insert=end`]: For lists. Accepts the literal: `start` (for queue) or `end` (for stack).
    - [`ex=-1`]: Expiry in seconds
    
**`exists(key)`**
: Check if the key exists.
: *Returns*: `bool`
: - `key`: Key name