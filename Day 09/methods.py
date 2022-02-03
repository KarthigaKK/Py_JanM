# """Regular methods, Class Methods and Static Methods"""

class Emp:

	raise_amt = 1.05
	num_of_emps = 0
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = f"{first.lower()}.{last.lower()}@company.com"

		Emp.num_of_emps += 1

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_str(cls, emp_str):
		first, last, pay = emp_str.split(' - ')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


emp_1 = Emp('John', 'K', 60000)
emp_2 = Emp('Jane', 'M', 70000)

import datetime

my_date = datetime.date(2022, 1, 30)

print(Emp.is_workday(my_date))

# emp_1_str = 'John - K - 60000'

# new_emp = Emp.from_str(emp_1_str)

# print(new_emp.pay)



# import datetime


# print(datetime.__file__)