import unittest

import sol3_1 as sol

class SwapTest(unittest.TestCase):

	def test_swap(self):
		a, b = 5, 3
		self.assertEqual((3, 5), sol.swap(a, b))
		self.assertEqual((5, 3), sol.swap(b, a))

unittest.main()