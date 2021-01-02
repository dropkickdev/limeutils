from limeutils import redis, parse_str

r = redis.Redis(pre='MOOLAH', ver='v42')

# r.hmset('peanuts', dict(a=1, b=2.4, c='shoo'))
# # x = r.hmget('peanuts')
# # print(x)
# r.hmset('peanuts', dict(d=None, e=0))
# r.hset('peanuts', 'f', None)
# x = r.hmget('peanuts')
# # print(x)



# # parse_str
# b = bytes()
# a = ['a1', '0', '000', '345', '6.4', b]
# for i in a:
#     i = parse_str(i)
#     print(i, type(i), bool(i))


# r.hset('abra', 'fed', 23)
# r.hset('abra', 'meh', 5.2)
# r.hset('abra', 'nothing', 0)
# r.hset('abra', 'zoom', None)
# # x = r.hmget('abra')
# x = r.hget('abra', 'nothing', 4)
# print(x, type(x), bool(x))

# print('----------------------------------------------')
# for k,v in x.items():
#     print(k, v, type(v), bool(v))


x = r.delete(['ddd', 'bbb'])
print(x)