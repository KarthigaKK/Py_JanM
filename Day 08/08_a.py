# Class and instances

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

print(Emp.num_of_emps)

emp_1 = Emp('John', 'K', 60000)
emp_2 = Emp('Jane', 'M', 70000)


print(Emp.num_of_emps)

# emp_1.raise_amt = 1.06

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.raise_amt)
# # print(emp_2.__dict__)

# # print(emp_1.__dict__)

# # print(emp_1.fullname())
# # print(Emp.fullname(emp_1))
# # print(emp_1.__dict__)

# # # print(emp_1.last)
# # # print(f"{emp_1.first} {emp_1.last}")
# # # print(f"{emp_2.first} {emp_2.last}")