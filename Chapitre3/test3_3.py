import unittest
import math

import sol3_3 as sol

class LongueurTest(unittest.TestCase):

	def test_longueur_1_points(self):
		p1 = (2, 3)
		self.assertEqual(0, sol.longueur(p1))

	def test_longueur_2_points(self):
		p1 = (2, 3)
		p2 = (4, 7)
		self.assertEqual((math.sqrt(2**2 + 4**2)), sol.longueur(p1, p2))

	def test_longueur_3_points(self):
		p1 = (2, 3)
		p2 = (4, 7)
		p3 = (5, 9)
		dist = math.sqrt(2**2 + 4**2) + math.sqrt(1 + 2**2)
		self.assertEqual(dist, sol.longueur(p1, p2, p3))

	def test_longueur_4_points(self):
		p1 = (2, 3)
		p2 = (4, 7)
		p3 = (5, 9)
		p4 = (7, 13)
		dist = math.sqrt(2**2 + 4**2) + math.sqrt(1 + 2**2) + math.sqrt(2**2 + 4**2)
		self.assertEqual(dist, sol.longueur(p1, p2, p3, p4))

unittest.main()