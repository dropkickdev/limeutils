import unittest, redis as mainredis
from limeutils import redis

class RedisTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.reds = mainredis.Redis()
        self.r = redis.Redis(pre='MOOLAH', ver='v42')
        self.r.hset('abra', 'foo', 'bar')
        self.r.hset('abra', 'fed', 23)
        self.r.hset('abra', 'meh', 5.2)
        self.r.hset('abra', 'nothing', 0)
        self.r.hset('abra', 'zoom', None)
        
        
    def test_hset(self):
        self.reds.delete('MOOLAH:v42:football')
        self.assertEqual(self.r.hset('football', 'team', 'chelsea'), 1)
        self.assertEqual(self.r.hset('football', 'team', 'barca'), 0)
        self.assertEqual(self.r.hset('football', '', ''), 1)


    def test_hmset(self):
        data1 = dict(aaa=1, bbb=2)
        data2 = dict(bbb=2, ccc=42)
        data3 = dict(bbb=54, ccc=42)
        self.reds.delete('MOOLAH:v42:foobar')
        
        x = self.r.hmset('foobar', mapping=data1)
        self.assertEqual(x, 2)
        x = self.r.hmset('foobar', mapping=data2)
        self.assertEqual(x, 1)
        x = self.r.hmset('foobar', mapping=data3)
        self.assertEqual(x, 0)
        x = self.r.hmset('foobar', mapping={})
        self.assertEqual(x, 0)
    
    
    def test_hget(self):
        self.assertEqual(self.r.hget('abra', 'foo', 4), 'bar')
        self.assertEqual(self.r.hget('abra', 'fed', 4), 23)
        self.assertEqual(self.r.hget('abra', '', 4), 4)
        self.assertEqual(self.r.hget('abra', 'zoom', 4), 4)
        self.assertEqual(self.r.hget('abra', 'oaeueoueou', 4), 4)
        self.assertEqual(self.r.hget('abra', 'nothing', 4), 0)


    def test_hmget(self):
        self.assertEqual(self.r.hmget('abra', ['foo', 'fed']), dict(foo='bar', fed=23))
        self.assertEqual(self.r.hmget('abra', ['nothing']), dict(nothing=0))
        self.assertEqual(self.r.hmget('abra', []), dict())
        self.assertEqual(self.r.hmget('abra'), dict(foo='bar', fed=23, meh=5.2, nothing=0, zoom=''))

 
    def test_hdel(self):
        data = dict(aaa=1, bbb=2, ccc=3, ddd=4, eee=5)
        self.r.hmset('mustard', data)
        self.assertEqual(self.r.hdel('mustard', 'ccc'), 1)
        self.assertEqual(self.r.hdel('mustard', 'xxx'), 0)
        self.assertEqual(self.r.hdel('mustard', ['aaa', 'bbb']), 2)
        self.assertEqual(self.r.hdel('mustard', ['ddd', 'zzz']), 1)
        
    
    def test_delete(self):
        self.r.hset('aaa', 'abc', 23)
        self.r.hset('bbb', 'abc', 23)
        self.r.hset('ccc', 'abc', 23)
        self.r.hset('ddd', 'abc', 23)
        self.r.hset('eee', 'abc', 23)
        self.assertEqual(self.r.delete('aaa'), 1)
        self.assertEqual(self.r.delete(['bbb', 'ccc']), 2)
        self.assertEqual(self.r.delete('ccc'), 0)
        self.assertEqual(self.r.delete(['eee']), 1)
        self.assertEqual(self.r.delete(''), 0)
        self.assertEqual(self.r.delete(['xxx', 'ddd']), 1)
        
    
    def test_set(self):
        self.reds.delete('MOOLAH:v42:sam')
        self.assertTrue(self.r.set('sam', 'abc'))
        self.assertTrue(self.r.set('sam', '123'))
        self.assertTrue(self.r.set('sam', 'foo'))
        self.assertTrue(self.r.set('sam', 'foo'))
        self.assertTrue(self.r.set('sam', ''))
        self.assertTrue(self.r.set('sam', None))
        
        
    def test_get(self):
        self.r.set('qqq', 'abc')
        self.r.set('www', '123')
        self.r.set('rrr', '')
        self.r.set('lll', None)
        self.assertEqual(self.r.get('qqq', 789), 'abc')
        self.assertEqual(self.r.get('www', 789), 123)
        self.assertEqual(self.r.get('rrr', 789), 789)
        self.assertEqual(self.r.get('lll', 789), 789)
        self.assertEqual(self.r.get('lll'), '')
        
    
        

if __name__ == '__main__':
    unittest.main()