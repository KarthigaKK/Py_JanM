import unittest
from employee import Emp


class TestEmp(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('SetUpClass')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass')

	def setUp(self):
		print('setUp\n')
		self.emp_1 = Emp('John','M',80000)
		self.emp_2 = Emp('Kate','K',90000)

	def tearDown(self):
		print('tearDown\n')


	def test_email(self):

		self.assertEqual(self.emp_1.email, 'john.m@company.com')
		self.assertEqual(self.emp_2.email, 'kate.k@company.com')

		self.emp_1.first = 'Jane'
		self.emp_2.first = 'Tom'

		self.assertEqual(self.emp_1.email, 'jane.m@company.com')
		self.assertEqual(self.emp_2.email, 'tom.k@company.com')

	def test_fullname(self):

		self.assertEqual(self.emp_1.fullname, 'John M')
		self.assertEqual(self.emp_2.fullname, 'Kate K')

		self.emp_1.first = 'Jane'
		self.emp_2.first = 'Tom'

		self.assertEqual(self.emp_1.fullname, 'Jane M')
		self.assertEqual(self.emp_2.fullname, 'Tom K')

	def test_apply_raise(self):

		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 84000)
		self.assertEqual(self.emp_2.pay, 94500)








if __name__ == '__main__':
	unittest.main()


