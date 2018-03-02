from name_function import get_formatted_name
import unittest

class NamesTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name = get_formatted_name('sUn','jIaN')
		self.assertEqual(formatted_name, 'Sun Jian')
	def test_last_first_name(self):
		formatted_name = get_formatted_name('sUn','jIaN')
		self.assertEqual(formatted_name, 'Sun Jian')
		
unittest.main()
