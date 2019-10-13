import unittest

import sol4_4 as sol

class AnagrammesTest(unittest.TestCase):

    def test_true(self):
        v = 'marion'
        w = "romina"
        self.assertEqual(True, sol.anagrammes(v, w))
    
    def test_len_v_gt_len_w(self):
        v = 'marionna'
        w = 'romina'
        self.assertEqual(False, sol.anagrammes(v, w))
    
    def test_false(self):
        v = "idis"
        w = 'hdgz'
        self.assertEqual(False, sol.anagrammes(v, w))

unittest.main()