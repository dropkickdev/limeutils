import unittest, pytest, redis as mainredis
from limeutils import Redis


@pytest.fixture(scope='session', autouse=True)
def delete_keys(r):
    # print('FOO')
    yield
    r.delete(['football', 'foobar', 'mustard', 'abra', 'sam', 'rrr', 'lll', 'qqq', 'www'])
    # print('BAR')
    
@pytest.fixture(scope='session')
def r():
    r = Redis(pre='MALICE', ver='v42')
    data(r)

    return r

@pytest.fixture(scope='session')
def reds():
    r = mainredis.Redis()
    return r

def data(r):
    # hmget
    r.hset('abra', 'foo', 'bar')
    r.hset('abra', 'fed', 23)
    r.hset('abra', 'meh', 5.2)
    r.hset('abra', 'nothing', 0)
    r.hset('abra', 'zoom', None)
    
    # hdel
    r.hmset('mustard', dict(aaa=1, bbb=2, ccc=3, ddd=4, eee=5))
    
    # delete
    r.hset('aaa1', 'abc', 23)
    r.hset('aaa2', 'abc', 23)
    r.hset('aaa3', 'abc', 23)
    r.hset('aaa4', 'abc', 23)
    r.hset('aaa5', 'abc', 23)
    
    # get
    r.set('qqq', 'abc')
    r.set('www', '123')
    r.set('rrr', '')
    r.set('lll', None)


param = [('football', 'team', 'chelsea', 1), ('football', 'team', 'barca', 0),
         ('football', '', '', 1)]
@pytest.mark.parametrize('k, f, v, out', param)
def test_hset(r, k, f, v, out):
    assert r.hset(k, f, v) == out


param = [(dict(bbb=2, ccc=42), 2), (dict(aaa=1, bbb=2), 1), (dict(bbb=54, ccc=42), 0), ({}, 0)]
@pytest.mark.parametrize('m, o', param)
def test_hmset(r, m, o):
    assert r.hmset('foobar', mapping=m) == o


param = [('foo', 4, 'bar'), ('fed', 4, 23), ('', 4, 4), ('zoom', 4, 4), ('nonexistent', 4, 4),
         ('nothing', 4, 0)]
@pytest.mark.parametrize('f, v, o', param)
def test_hget(r, f, v, o):
    assert r.hget('abra', f, v) == o


param = [(['foo', 'fed'], dict(foo='bar', fed=23)), (['nothing'], dict(nothing=0)),
         ([], {}), (None, dict(foo='bar', fed=23, meh=5.2, nothing=0, zoom=''))]
@pytest.mark.parametrize('k, o', param)
def test_hmget(r, k, o):
    assert r.hmget('abra', k) == o


param = [('ccc', 1), ('xxx', 0), (['aaa', 'bbb'], 2), (['ddd', 'zzz'], 1)]
@pytest.mark.parametrize('k, out', param)
def test_hdel(r, k, out):
    assert r.hdel('mustard', k) == out


param = [('aaa1', 1), (['aaa2', 'aaa3'], 2), ('aaa3', 0), (['aaa5'], 1), ('', 0),
         (['xxx', 'aaa4'], 1)]
@pytest.mark.parametrize('k, out', param)
def test_delete(r, k, out):
    assert r.delete(k) == out


param = ['abc', '123', 'foo', 'foo', '', None]
@pytest.mark.parametrize('k', param)
def test_set(r, k):
    assert r.set('sam', k) is True


param = [('qqq', 789, 'abc'), ('www', 789, 123), ('rrr', 789, 789), ('lll', 789, 789),
         ('lll', None, '')]
@pytest.mark.parametrize('k, v, out', param)
def test_get(r, k, v, out):
    if v is not None:
        assert r.get(k, v) == out
    else:
        assert r.get(k) == out
