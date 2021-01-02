import unittest
from limeutils import redis

class RedisTest(unittest.TestCase):
    
    def test_hget(self):
        r = redis.Redis(pre='MOOLAH', ver='v42')
        r.hset('abra', 'fed', 23)
        r.hset('abra', 'meh', 5.2)
        r.hset('abra', 'nothing', 0)
        r.hset('abra', 'zoom', None)
        
        self.assertEqual(r.hget('abra', 'fed', 4), 23)
        self.assertEqual(r.hget('abra', '', 4), 4)
        self.assertEqual(r.hget('abra', 'zoom', 4), 4)
        self.assertEqual(r.hget('abra', 'oaeueoueou', 4), 4)
        self.assertEqual(r.hget('abra', 'nothing', 4), 0)

 

if __name__ == '__main__':
    unittest.main()