import unittest

import sol4_3 as sol

class PGBTest(unittest.TestCase):

    def test_2_bords(self):
        w = "abdaabda"
        self.assertEqual("abda", sol.plus_grand_bord(w))
    
    def test_1_bord(self):
        w = "ablabda"
        self.assertEqual("a", sol.plus_grand_bord(w))
    
    def test_0_bord(self):
        w = "idis"
        self.assertEqual("", sol.plus_grand_bord(w))

unittest.main()
