import unittest

import sol3_9 as sol

class DureeTest(unittest.TestCase):

	def test_h1_avant_h2(self):
		# gt = great than 
		h1 = (14, 39)
		h2 = (18, 45)
		self.assertEqual((4, 6), sol.duree(h1, h2))
	
	def test_h1_apres_h2(self):
		h1 = (6, 0)
		h2 = (5, 15)
		self.assertEqual((23, 15), sol.duree(h1, h2))


unittest.main()