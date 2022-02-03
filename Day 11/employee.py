# property decorators


class Emp:

	raise_amt = 1.05

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

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

		