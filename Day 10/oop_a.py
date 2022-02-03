# property decorators


class Emp:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		# self.email = f"{first.lower()}.{last.lower()}@company.com"

	@property
	def fullname(self):
		return f"{self.first} {self.last}"

	@property
	def email(self):
		return f"{self.first.lower()}.{self.last.lower()}@company.com"

	def __repr__(self):
		return f"Emp('{self.first}', '{self.last}', {self.pay})"

	def __str__(self):
		return f"{self.fullname} - {self.pay}"


emp_1 = Emp('John', 'K', 60000)

print(repr(emp_1))
print(str(emp_1))