def square(x):
	return x * x

def cube(x):
	return x * x * x

lst = [1,2,3,4]

def my_sq(func, lst_args):
	result = []
	for i in lst:
		result.append(func(i))
	return result

print(my_sq(square, lst))
print(my_sq(cube, lst))

# print(square(lst))



# result = square
# print(result(6))


'''
first-class functions 
if it treats functions as first-class citizens. 

This means the language supports passing functions as arguments to other functions, 
returning them as the values from other functions, and 
assigning them to variables or storing them in data structures
'''


