from city_functions import get_formatted_city
import unittest

class CitiesTestCase(unittest.TestCase):
	def test_city_format(self):
		formatted_city = get_formatted_city('bei jing','china')
		self.assertEqual(formatted_city, 'Bei Jing, China')
	def test_city_country_population(self):
		formatted_result = get_formatted_city('bei jing','china','20000000')
		self.assertEqual(formatted_result, 'Bei Jing, China 20000000')
		
unittest.main()
