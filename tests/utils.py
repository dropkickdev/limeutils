import unittest
from limeutils import utils, redis


class UtilsTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.r = redis.Redis(pre='MOOLAH', ver='v42')
        self.r.hmset('abra', dict(fed=23, meh=5.2, nothing=0, zoom=None))
    
    def test_isfloat(self):
        self.assertTrue(utils.isfloat(3))
        self.assertTrue(utils.isfloat(3.0))
        self.assertTrue(utils.isfloat(0))
        self.assertTrue(utils.isfloat('3.4'))
        self.assertTrue(utils.isfloat('0.4'))
        self.assertTrue(utils.isfloat('0.0'))
        self.assertTrue(utils.isfloat('0'))
        self.assertTrue(utils.isfloat('3.0'))
        self.assertTrue(utils.isfloat('3'))
        self.assertFalse(utils.isfloat('abc'))
        self.assertFalse(utils.isfloat('3,344'))
        self.assertFalse(utils.isfloat('3,344.5'))
        self.assertFalse(utils.isfloat('3,344.00'))
    
    def test_parse_str(self):
        self.assertEqual(utils.parse_str('123'), 123)
        self.assertEqual(utils.parse_str('12.3'), 12.3)
        self.assertEqual(utils.parse_str('a1b2c3'), 'a1b2c3')
        self.assertEqual(utils.parse_str('abc'), 'abc')
        self.assertEqual(utils.parse_str(''), '')
        self.assertEqual(utils.parse_str('-'), '-')
        with self.assertRaises(ValueError):
            utils.parse_str(None)       # noqa
            utils.parse_str(bytes())    # noqa
    
    def test_byte_conv(self):
        x = self.r.hget('abra', 'fed')
        self.assertEqual(utils.byte_conv(x), 23)
        x = self.r.hget('abra', 'meh')
        self.assertEqual(utils.byte_conv(x), 5.2)
        x = self.r.hget('abra', 'nothing')
        self.assertEqual(utils.byte_conv(x), 0)
        x = self.r.hget('abra', 'zoom')
        self.assertEqual(utils.byte_conv(x), '')
        
    def test_split_fullname(self):
        self.assertEqual(utils.split_fullname('Hey You'), ('Hey', 'You'))
        self.assertEqual(utils.split_fullname('Sir Hey You'), ('Sir Hey', 'You'))
        self.assertEqual(utils.split_fullname('Sir Hey You Phd'), ('Sir Hey', 'You Phd'))
        self.assertEqual(utils.split_fullname('Hey delos You'), ('Hey', 'delos You'))
        self.assertEqual(utils.split_fullname('Hey san You'), ('Hey', 'san You'))
        self.assertEqual(utils.split_fullname('Eliza Maria Erica dona Aurora Phd Md'),
                         ('Eliza Maria Erica', 'dona Aurora Phd Md'))
        
            
if __name__ == '__main__':
    unittest.main()
