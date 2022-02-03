# def demo_func(greeting, name='You'):
# 	return f"{greeting} - {name}"


def emp_info(*sdss, **sdva):
	print(sdss)
	print(sdva)

emp_info('Hello', 'Hi', 'Bye' , name='John', age=27)