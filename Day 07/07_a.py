# def outer_func(message):
# 	def inner_func():
# 		print(message)

# 	return inner_func()


# Hello_func = outer_func('Hello')
# # Hello_func
# Hi_func = outer_func('Hi')
# print(result.__name__)
# Hi_func()


def decorator_function(func):
	def wrapper_function(*args, **kwargs):
		print('hello')
		return func(*args, **kwargs)
	return wrapper_function

@decorator_function
def display():
	print('display function ran!')

@decorator_function
def display_info(name, age):
	print(f'display_info ran with args ({name} - {age})')

display_info('John', 27)


# decorated_disp = decorator_function(display)

# decorated_disp()


# display()