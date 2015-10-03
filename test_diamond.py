import unittest
import diamond

class TestQueryAdDetail(unittest.TestCase):


    def test_input_A_return_A(self):
        d = diamond.Diamond()
        assert d.print_diamond('A') == 'A'

    def test_input_B_return_diamond_AB(self):
        d = diamond.Diamond()
        assert d.print_diamond('B') ==  ' A\n'\
                                        'B B\n'\
                                        ' A'

    def test_input_C_return_diamond_A_to_C(self):
        d = diamond.Diamond()
        assert d.print_diamond('C') ==  '  A\n'\
                                        ' B B\n'\
                                        'C   C\n'\
                                        ' B B\n'\
                                        '  A'