Redis API
=========
 
**`get(key, **kwargs)`**
: Get the value of a key. To set the value of this key use **`set()`**.
: *Returns*: Can be `string`, `int`, `float`, `byte`, `dict`, `list`, or `set`.

: - `key`: `str` key name
- `kwargs`: Choose from any of the custom keys below.
    - `start=0`: Starting index for lists
    - `end=-1`: Ending index for lists
    - `only=`: For hashes only return the fields you need

**`set(key, val, **kwargs)`**
: Create or update a new key. To read this key use **`get()`**.
: *Returns*: Varied depending on the value you set.

: - `key`: `str` key name
- `val`: Can be `string`, `int`, `float`, `byte`, `dict`, `list`, or `set`
- `kwargs`: Custom keys set below. Accepts all other keys set in the parent redis package.
    - `clear=False`: Delete the key first instead of updating it (if `dict` or `list`)
    - `insert=end`: For lists. Accepts the literal: `start` (for queue) or `end` (for stack).
    - `ex=-1`: Expiry in seconds
    
**`exists(key)`**
: Check if the key exists.
: *Returns*: `bool`
: - `key`: `str` key name