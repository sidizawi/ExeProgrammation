import unittest
import math

import sol3_5 as sol

class RacineTest(unittest.TestCase):

	def test_1_racine(self):
		# x² + 2x + 1 = (x + 1)²  
		alpha = 1
		beta = 2
		gamma = 1
		self.assertEqual([-1], sol.rac_eq_2nd_deg(alpha, beta, gamma))

	def test_2_racine(self):
		# x² + 3x + 2
		alpha = 1
		beta = 3
		gamma = 2
		self.assertEqual([-1, -2], sol.rac_eq_2nd_deg(alpha, beta, gamma))

	def test_racine_complexe(self):
		# x² + x + 1 
		alpha = 1
		beta = 1
		gamma = 1
		self.assertEqual(None, sol.rac_eq_2nd_deg(alpha, beta, gamma))

unittest.main()