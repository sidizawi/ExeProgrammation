import unittest

import sol3_11 as sol

class SumTest(unittest.TestCase):

	def test_sum_positif(self):
		a, b = 5, 2
		self.assertEqual(7, sol.sum(a, b))

	def test_sum_negatif(self):
		a,b = -5, -6
		self.assertEqual(-11, sol.sum(a, b))

	def test_sum_both(self):
		a, b = -2, 4
		self.assertEqual(2, sol.sum(a, b))

unittest.main()