Utilities
=========

Utilities API
-------------

**`isfloat(val)`**
: Checks if the contents of a string is a float.
: *Returns*: `bool`
: - `val`: String to check if it contains a float

**`byte_conv(val)`**
: Converts bytes to a python string. This string could later be parsed into the correct
      python data type using `parse_str()`. Used mostly with Redis return values which always return in
      bytes.
: *Returns*: `str`
: - `val`: Bytes value to convert

**`parse_str(string)`**
: Converts a string to either an int, float, or str depending on its value. Does not support
 pickled values as you'll have to convert those separately. Works well with `byte_conv()`.
: *Returns*: String to convert
: - `string`: `int`, `float`, or `str`

**`split_fullname(fullname, default='', prefix=None, suffix=None)`**
: Splits a fullname into their respective first_name and last_name fields.
      If only one name is given, that becomes the first_name
: *Returns*: `tuple` containing the firstname and the lastname
: - `fullname`: The name to split
- `default`: The value if only one name is given
- `prefix`: Custom prefixes to append to the default list
- `suffix`: Custom suffixes to append to the default list

```python
fullname = 'Eliza Maria Erica dona Aurora Phd Md'
firstname, lastname = split_fullname(fullname)

print(firstname)
# Eliza Maria Erica

print(lastname)
# dona Aurora Phd Md
```

Database API
------------

**`model_str(instance, attr)`**
: The attribute to display for an object's `__str__`. If the attribute doesn't exist then an
 alternative will be displayed. Commonly used for ORMs but can be applied anywhere with classes.

: *Returns*: String name

: - `instance`: Object of the class
- `attr`: Attribute of that object you want to use for its `__str__`

**`modstr(instance, attr)`**

: Alias for `model_str().`

**`classgrabber(dotpath)`**
: Import a class from a dot path string.
      
: *Returns*: The class itself which is found at the end of the dot path.

: *Example:*
```
# Import the Settings class from a string
Settings = classgrabber('app.folder.file.Settings')

# Settings class now ready for use
myobj = Settings()
```

