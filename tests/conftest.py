import pytest
from limeutils import Red
from icecream import ic





@pytest.fixture(scope='session')
def red():
    conf = {
        # 'host': 'localhost',
        # 'port': 6379,
        'db': 1,
        'pre': 'TEST',
        'ver': '',
        'ttl': 3600 * 24 * 15,
    }
    yield Red(**conf)


@pytest.fixture(scope='session')
def nooverwrite():
    conf = {
        # 'host': 'localhost',
        # 'port': 6379,
        'db': 1,
        'pre': 'TEST',
        'ver': '',
        'ttl': 3600 * 24 * 15,
        'wrongtype': False
    }
    return Red(**conf)

@pytest.fixture(scope='module')
def keypatterns(red):
    red.flushdb()
    red.set('play-xxx-aaa', '')
    red.set('play-xxx-bbb', '')
    red.set('play-yyy-ccc', '')
    red.set('play-yyy-ddd', '')
    # def foo():
    # return foo



#
#
# @pytest.fixture(scope='session', autouse=True)
# def delete_keys(r):
#     # print('FOO')
#     yield
#     r.delete(['football', 'foobar', 'mustard', 'abra', 'sam', 'rrr', 'lll', 'qqq', 'www'])
#     # print('BAR')
#
# def data(r):
#     # hmget
#     r.hset('abra', 'foo', 'bar')
#     r.hset('abra', 'fed', 23)
#     r.hset('abra', 'meh', 5.2)
#     r.hset('abra', 'nothing', 0)
#     r.hset('abra', 'zoom', None)
#
#     # hdel
#     r.hmset('mustard', dict(aaa=1, bbb=2, ccc=3, ddd=4, eee=5))
#
#     # delete
#     r.hset('aaa1', 'abc', 23)
#     r.hset('aaa2', 'abc', 23)
#     r.hset('aaa3', 'abc', 23)
#     r.hset('aaa4', 'abc', 23)
#     r.hset('aaa5', 'abc', 23)
#
#     # get
#     r.set('qqq', 'abc')
#     r.set('www', '123')
#     r.set('rrr', '')
#     r.set('lll', None)