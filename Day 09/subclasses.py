# Class and instances

class Emp:

	raise_amt = 1.05
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = f"{first.lower()}.{last.lower()}@company.com"
		
	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)


class Developer(Emp):
	raise_amt = 1.09

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(Emp):

	def __init__(self, first, last, pay, employees =None):
		super().__init__(first, last, pay)

		if employees is None:
			self.employees = []
		else:
			self.employees = employees


	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def display_emp(self):
		for emp in self.employees:
			print(emp.fullname())


emp_1 = Emp('John', 'K', 60000)
dev_1 = Developer('Jane', 'M', 70000, 'Python')
mgr = Manager('Tom', 'H', 90000)

# mgr.add_emp(dev_1)
# mgr.add_emp(emp_1)

# mgr.remove_emp(dev_1)

# mgr.display_emp()


print(issubclass(Manager, Emp))
print(isinstance(mgr, Developer))