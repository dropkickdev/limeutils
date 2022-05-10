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

Setup
-----

### Use Default settings
```python
from limeutils import Red

r = Red()
```

### Use custom config
```python
from limeutils import Red

CACHE_CONFIG = {
    'pre':  'FOOBAR',
    'ver':  'v1',
    'ttl':  3600,
}
r = Red(**CACHE_CONFIG)
```
- `pre`: Prefix for your key. Defaults to an empty string.
- `ver`: Version for your key. Defaults to an empty string.
- `ttl`: Expires time for the key. Can be overridden in the `set()` method. Defaults to -1.
- `clear_wrongtype`: Allows using an existing key for a different data type (e.g. string -> dict
). Defaults to `True`. Setting this to `False` raises an exception whenever you try saving with
 a different data type than the one you started with.

### With connection information

```python
from limeutils import Red

CACHE_CONFIG = {
    'host': 'localhost',
    'port': 6379,
    'db':   0,
    'pre':  'FOOBAR',
    'ver':  'v1',
    'ttl':  3600
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

Keys are saved in the format **prefix:version:key** in redis. Creating a key named `user` in python is saved as `FOOBAR:v1:user` in redis. But when
  you need to use this key in python you only type the name `user` and the `r` object
  prepends the prefixes for you.    
