import unittest 

import sol4_5 as sol

class IntersectionTest(unittest.TestCase):

    def test_gramm(self):
        v = 'programme'
        w = 'grammaire'
        self.assertEqual("gramm", sol.intersection(v, w))
    
    def test_0_inter(self):
        v = 'pro'
        w = 'aire'
        self.assertEqual('', sol.intersection(v, w))

unittest.main()