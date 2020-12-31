from limeutils import redis

r = redis.Redis(prefix='MOOLAH', version='v42')
# x = r.hset('abra', 'fed', 'cadabra', ttl=30)
x = r.hmset('magic', dict(a=1, b='shoo', c=3.6), ttl=60, pre='SUM')
print(x)