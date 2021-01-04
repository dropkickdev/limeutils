Redis
=====

Setup
-----

The `Redis` class uses the official `redis` package to implement its methods. This class acts as
 a wrapper for it silently parsing all data coming from your redis database into python
  data types.

```py
from limeutils import redis

# Create the redis object
r = redis.Redis(pre='FOOBAR', ver='v1')
```
- `pre`: Prefix for your project. Defaults to an empty string.
- `ver`: Version for your key. Defaults to an empty string.

You can add details about your connection in `Redis()`. In this case only the default settings
 are being used.
 
Adding redis connection info:
 
```py
from limeutils import redis

r = redis.Redis(host='localhost', port=2468, db=0, pre='FOOBAR', ver='v1')
```
 
#### Key prefixing

It's recommended to use key prefixing in redis so including the `pre` and `ver` attributes does this for you. For example, the key `user-123` is saved as **FOOBAR:v1:user-123** but in your code you just type in `user-123` and not the prefixed version.

If you don't want to add any prefixing to your keys then just don't add them when instantiating your object: `r = redis.Redis()`.


### Quickstart
```python
from limeutils import redis

# Create the redis object
r = redis.Redis(pre='FOOBAR', ver='v1')

# Save a key
r.set('samplekey', 'hello there')

# Read the key
message = r.get('samplekey')

# Save a hash
r.hset('user-123', 'username', 'jimisthebomb')

# Read the hash
username = r.hget('user-123', 'username')
```

## Methods
All methods are accessible from an instance of the `Redis` class. All methods are validated using
 the `pydantic` package.
 
 Below are some custom data types used to make the code shorter.
 ```python
from typing import Union

# Custom data types
LT = Union[list, tuple]
V = Union[str, int, float, bytes]
```
The `LT` and `V` data types are used throughout this package.

`get()`
Something

`hget()`
Something

`hmget()`
Something

`hmset()`
Something

`hset()`
Something


`set(key: str, val: V, xx: bool = False, keepttl: bool = False, ttl=None, pre=None, ver=None
)`{:.python}


- `key`: Key name
- `val`: Key value
- `xx`: Set to val only if key already exists
- `keepttl`: Retain the time to live associated with the key.
- `ttl`: TTL for this key. Can be in `int` seconds or a `timedelta` object.
- `pre`: Custom prefix. Overrides the *pre* set in `Redis()`
- `ver`: Custom version. Overrides the *ver* set in `Redis()`

`hget()`
