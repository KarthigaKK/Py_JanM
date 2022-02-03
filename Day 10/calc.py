def add(x, y):
	""" add function """
	return x + y 

def sub(x, y):
	""" add function """
	return x - y 

def multiply(x, y):
	""" add function """
	return x * y 

def divide(x, y):
	if y == 0:
		raise ValueError("Can't divide by zero!")
	return x/y


# print(divide(5,2))

# print(add(2,2))