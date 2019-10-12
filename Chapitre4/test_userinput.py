import unittest

import userinput as sol

class ConvertIntTest(unittest.TestCase):

	def test_s_int(self):
		s = '54'
		self.assertEqual(54, sol.convert_to_int(s))

	def test_s_float(self):
		s = "52.36"
		self.assertEqual(None, sol.convert_to_int(s))

	def test_s_str(self):
		s = "me54220zff"
		self.assertEqual(None, sol.convert_to_int(s))

class ConvertFloatTest(unittest.TestCase):

	def test_s_float(self):
		s = "54.36"
		self.assertEqual(54.36, sol.convert_to_float(s))

	def test_s_str(self):
		s = "kjof688rf,lkv"
		self.assertEqual(None, sol.convert_to_float(s))

	def test_s_int(self):
		s = "5"
		self.assertEqual(5, sol.convert_to_float(s))

class IsOneWordTest(unittest.TestCase):

	def test_one_word(self):
		s = "me"
		self.assertEqual(True, sol.is_one_word(s))

	def test_2_words(self):
		s = "he is"
		self.assertEqual(False, sol.is_one_word(s))

class IsOneLetterTest(unittest.TestCase):

	def test_1_letter(self):
		s = 's'
		self.assertEqual(True, sol.is_one_letter(s))

	def test_2_letter(self):
		s = 'idis'
		self.assertEqual(False, sol.is_one_letter(s))

	def test_1_letter_2_word(self):
		s = "d f"
		self.assertEqual(False, sol.is_one_letter(s))

unittest.main()
