import unittest

import sol3_10 as sol

class AplliquerTest(unittest.TestCase):

	def test_appliquer_som(self):
		som = lambda a, b : a + b
		a, b = 5, 6
		self.assertEqual(11, sol.appliquer(a, b, som))

	def test_appliquer_subs(self):
		subs = lambda a, b : a - b
		a, b = 20, 15
		self.assertEqual(5, sol.appliquer(a, b, subs))

	def test_appliquer_mult(self):
		mult = lambda a, b : a*b
		a, b = 5, 6
		self.assertEqual(30, sol.appliquer(a, b, mult))

	def test_appliquer_div(self):
		div = lambda a, b : a/b
		a, b = 30, 5
		self.assertEqual(6, sol.appliquer(a, b, div))

	def test_appliquer_exp(self):
		exp = lambda a, b : a**b
		a, b = 2, 10
		self.assertEqual(1024, sol.appliquer(a, b, exp))

unittest.main()