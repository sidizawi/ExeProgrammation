import unittest

import sol3_7 as sol

class RendreMonnaieTest(unittest.TestCase):

	def test_monnaie_pas_suffisante(self):
		prix = 51
		monnaie = (2, 1, 0, 0, 0)
		res = None
		self.assertEqual(res, sol.rendreMonnaie(prix, monnaie))

	def test_monnaie_egale_au_prix(self):
		prix = 51
		monnaie = (2, 1, 0, 0, 1)
		res = (0, 0, 0, 0, 0)
		self.assertEqual(res, sol.rendreMonnaie(prix, monnaie))

	def test_monnaie_plus_que_prix(self):
		prix = 51
		monnaie = (2, 1, 1, 0, 0)
		res = (0, 0, 0, 2, 0)
		self.assertEqual(res, sol.rendreMonnaie(prix, monnaie)) 

unittest.main()