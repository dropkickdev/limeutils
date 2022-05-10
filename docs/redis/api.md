Redis API
=========
 
**`formatkey(key)`**
: Create the key name in **prefix:version:key** format as it is  saved in redis.
: *Returns*: `str`

: - `key`: `str` key name

**`get(key, **kwargs)`**
: Get the value of a key. To set the value of this key use **`set()`**.
: *Returns*: `string`, `int`, `float`, `byte`, `dict`, `list`, or `set`.

: - `key`: `str` key name
- `kwargs`: Choose from any of the custom keys below.
    - `start=0`: Starting index for lists
    - `end=-1`: Ending index for lists
    - `only=`: For hashes only. Return the fields you need. List fields as a `list`.

**`set(key, val, **kwargs)`**
: Create or update a new key. To read this key use **`get()`**.
: *Returns*: Varied depending on the value you set.

: - `key`: `str` key name
- `val`: `string`, `int`, `float`, `byte`, `dict`, `list`, or `set`
- `kwargs`: Custom keys set below. Accepts all other keys set in the parent redis package.
    - `clear=False`: Delete the key first instead of updating it (if `dict` or `list`)
    - `insert=end`: For lists. Accepts the literal: `start` (for queue) or `end` (for stack).
    - `ttl=-1`: Expiry in seconds. Set to -1 for a key with no expiry. Defaults to the value you
     set when instantiating `Red()`. If no *ttl* value is set in `Red()` default is -1.
    
**`exists(*keys)`**
: Checks if keys exists. Returns the number of keys that exist *not* which of the keys exists.
: *Returns*: `int`
: - `*keys`: `str` key name