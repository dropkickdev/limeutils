import pytest
from limeutils import utils, Redis


param = [(3, True), (3.0, True), (0, True), ('3.4', True), ('0.4', True), ('0.0', True),
         ('0', True), ('3.0', True), ('3', True), ('abc', False), ('3,344', False),
         ('3,344.5', False), ('3,344.00', False)]
@pytest.mark.parametrize('val, out', param)
def test_isfloat(val, out):
    assert utils.isfloat(val) is out
    
    
param = [('123', 123), ('12.3', 12.3), ('a1b2c3', 'a1b2c3'), ('abc','abc'), ('', ''), ('-', '-'),
         (None, ValueError), (bytes(), ValueError)]
@pytest.mark.parametrize('val, out', param)
def test_parse_str(val, out):
    try:
        assert utils.parse_str(val) == out
    except out:
        with pytest.raises(out):
            assert utils.parse_str(val)
            
            
param = [('Hey You', ('Hey', 'You')), ('Sir Hey You', ('Sir Hey', 'You')),
         ('Sir Hey You Phd', ('Sir Hey', 'You Phd')), ('Hey delos You', ('Hey', 'delos You')),
         ('Hey san You', ('Hey', 'san You')),
         ('Eliza Maria Erica dona Aurora Phd Md', ('Eliza Maria Erica', 'dona Aurora Phd Md'))]
@pytest.mark.parametrize('val, out', param)
def test_split_fullname(val, out):
    assert utils.split_fullname(val) == out


param = [('abra', 'fed', 23), ('abra', 'meh', 5.2), ('abra', 'nothing', 0), ('abra', 'zoom', '')]
@pytest.mark.parametrize('key, val, out', param)
def test_byte_conv(r, key, val, out):
    x = r.hget(key, val)
    assert utils.byte_conv(x) == out
