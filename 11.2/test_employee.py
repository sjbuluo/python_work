from employee import Employee

import unittest

class EmployeeTest(unittest.TestCase):
	def setUp(self):
		e = Employee('Jian', 'Sun', 15000)
		self.e = e
		
	def test_give_default_raise(self):
		self.e.give_raise()
		self.assertEqual(self.e.yearly_salary, 20000)
		
	def test_give_custom_raise(self):
		self.e.give_raise(10000)
		self.assertEqual(self.e.yearly_salary, 25000)
		
unittest.main()
