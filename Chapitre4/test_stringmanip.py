import unittest

import stringmanip as sol

class CaractereTest(unittest.TestCase):

	def test_i_lt_len_s(self):
		s = "I love python"
		i = 5
		self.assertEqual("e", sol.caractere(s, i))

	def test_i_not_gt_len_s(self):
		s = 'I want to became...'
		i = len(s) + 5
		self.assertEqual("", sol.caractere(s, i))

class CaracteresTest(unittest.TestCase):

	def test_i_j(self):
		s = "Hello I'am idis"
		i, j = 0, 3
		self.assertEqual("Hell", sol.caracteres(s, i, j))
		i, j = -2, 4
		self.assertEqual("", sol.caracteres(s, i, j))
		s = "My name is idis"
		i, j = 5, len(s) + 27
		self.assertEqual("", sol.caracteres(s, i, j))
		i, j = len(s) +2, 5
		self.assertEqual("", sol.caracteres(s, i, j))

class ChangeCaracTest(unittest.TestCase):

	def test_change_caractere_i_in_s(self):
		s = "It's me"
		i = 1
		a = 'l'
		self.assertEqual("Il's me", sol.change_caractere(s, i, a))

	def test_change_caractere_i_not_in_s(self):
		s = "My name is idis"
		i = len(s) + 64
		a = 'd'
		self.assertEqual('', sol.change_caractere(s, i, a))

	def test_change_caractere_a_gt_1(self):
		s = "It's me again"
		i = 5
		a = "and me"
		self.assertEqual("", sol.change_caractere(s, i, a))

class ChangeCaracsTest(unittest.TestCase):

	def test_i_j_in_s(self):
		s = "It's me"
		i, j = 0, 1
		t = "He"
		self.assertEqual("He's me", sol.change_caracteres(s, i, j, t))

	def test_i_j_not_in_s(self):
		s = "Hello, World!"
		i, j = 0, len(s) + 6
		t = "la terre"
		self.assertEqual("", sol.change_caracteres(s, i, j, t))

class TrouveCaracTest(unittest.TestCase):

	def test_a_in_s(self):
		s = "I love Cambridge"
		a = "l"
		self.assertEqual(2, sol.trouve_caractere(s, a))

	def test_a_not_in_s(self):
		s = "I love Cambridge"
		a = "S"
		self.assertEqual(-1, sol.trouve_caractere(s, a))

	def test_compare_last_funct_trouve_caract(self):
		s = "I love Cambridge"
		a = "l"
		self.assertEqual(sol.trouve_caractere_avec_find(s, a), sol.trouve_caractere(s, a))


unittest.main()
