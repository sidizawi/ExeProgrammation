import unittest 
import math

import sol3_4 as sol

class ParallelogrammeTest(unittest.TestCase):

	def test_cotes_pas_egaux(self):
		p1 = (0, 1)
		p2 = (1, 2)
		p3 = (1, 0)
		p4 = (0, 0)
		self.assertEqual(None, sol.parallelogramme(p1, p2, p3, p4))

	def test_cotes_egaux(self):
		p1 = (0, 1)
		p2 = (1, 1)
		p3 = (1, 0)
		p4 = (0, 0)
		self.assertEqual(4, sol.parallelogramme(p1, p2, p3, p4))


unittest.main()