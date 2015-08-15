import sys
sys.path.insert(0, '../prtone')
import coin_toss

class TestClass():
    def test_flip_coin_returns_1or0(self):
        result = coin_toss.flip_coin()
        options = [1, 0]
        assert result in options
        
    def test_keep_flipping_returns_dictionary(self):
        r = 1
        flip_count = coin_toss.keep_flipping(r)
        assert flip_count[r] >= 2
        
    def test_take_average_does_exactly_that(self):
        stuff = {0:[1,2,3], 1:[2,3,4]}
        avg = coin_toss.take_average(stuff)
        assert int(avg[0]) == 2
        assert int(avg[1]) == 3
    
    def test_do_the_thing_returns_int(self):
        a_number = coin_toss.do_the_thing(5)
        assert type(a_number) == float
    
    def test_coin_toss_final_result(self):
        result = coin_toss.do_many_times(100, 100)
        assert 3.0 == round(result, 1)

import unittest

class CoinTossUnitTest(unittest.TestCase):
    def test_coin_toss_returns_float(self):
        result = coin_toss.do_many_times(100, 100)
        assert type(result) == float
        assert 2.8 < result < 3.2