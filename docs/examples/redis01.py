from limeutils import redis

# Create the redis object
r = redis.Redis(pre='FOOBAR', ver='v1')

# Save a key
r.set('samplekey', 'hello there')

# Read the key
message = r.get('samplekey')

# Save a hash
r.hset('user-123', 'username', 'jimisawesome')

# Read the hash
username = r.hget('user-123', 'username')