from limeutils import Red

# Create the redis object
r = Red()

# Save and read a key
r.set('message', 'Hello there')
r.get('message')                    # Returns int, float, string, or bytes
r.update('message', 'Ahoy')

# Save and read a hash
r.set('user', dict(username='jimmy', age=99, gender='m'))
r.get('user')                               # All keys as dict
r.get('user', fields=['username', 'age'])   # Some keys as dict
r.update('user', dict(username='sam'))

# Save and read a list
r.set('names', ['jimmy', 'tina'])
r.get('names')                              # Return list
r.update('names', ['sally'])
r.update('names', ['jeff'], insert='start')

# Save and read a set
r.set('names', {'jimmy', 'tina'})
r.get('names')                              # Return set