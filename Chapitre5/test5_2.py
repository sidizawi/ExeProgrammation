import unittest

import sol5_1 as sol

class BornesTest(unittest.TestCase):

    def test(self):
        nbr = [5, 6, 1, 3]
        self.assertEqual((1, 6), sol.bornes(nbr))
        nbr = [330, 548, 62, 0]
        self.assertEqual((0, 548), sol.bornes(nbr))

unittest.main()