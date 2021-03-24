from limeutils import Red

# Create the redis object
r = Red()

# STRING
r.set('message', 'Hello there')
r.get('message')                    # 'Hello there'
r.set('age', 5)
r.get('age')                        # 5 (int)
r.set('total', 12.5)
r.get('total')                      # 12.5 (float)

# HASH
r.set('user', dict(username='jimmy', age=99, gender='m'))
r.get('user')                               # dict(username='jimmy', age=99, gender='m')
r.set('user', dict(username='foo'))         # Update
r.get('user', only=['username', 'age'])     # dict(username='foo', age=99)

# LIST
r.set('names', ['jimmy', 'tina'])
r.set('names', ['sam'])
r.get('names')                              # ['jimmy', 'tina', 'sam']
r.get('names', start=1, end=-1)             # ['tina', 'sam']

# Save and read a set
r.set('names', {'jimmy', 'tina'})
r.get('names')                              # {'jimmy', 'tina'}