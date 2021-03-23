from limeutils import Red

# Create the redis object
r = Red()

# Save and read a key
r.set('message', 'Hello there')
r.get('message')                    # Returns int, float, string, or bytes

# Save and read a hash
r.set('user', dict(username='jimmy', age=99, gender='m'))
r.get('user')                               # All keys as dict
r.get('user', only=['username', 'age'])   # Some keys as dict

# Save and read a list
r.set('names', ['jimmy', 'tina'])
r.get('names')                              # Return list

# Save and read a set
r.set('names', {'jimmy', 'tina'})
r.get('names')                              # Return set