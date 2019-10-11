import unittest
import math 

import sol3_2 as sol

class DistanceTest(unittest.TestCase):

	def test_distancePoints(self):
		p1 = (2, 3)
		p2 = (4, 7)
		self.assertEqual((math.sqrt(2**2 + 4**2)), sol.distancePoints(p1, p2))

unittest.main()