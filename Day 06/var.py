# LEGB - local, Enclosing, Global, Builtins

# x = 'global x'

# def demo(z):
# 	# global x
# 	x = 'local x'
# 	print(z)

# demo('local z')
# print(x)


# import builtins

# # print(dir(builtins))

# # def max():
# # 	pass

# nums = [10,2,1,3,4,5]

# print(max(nums))

# # print(help(max))

x = 'global x'

def outer():
	x = 'outer x'

	def inner():
		# nonlocal x
		x = 'inner x'
		print(x)
	inner()

	print(x)

outer()
print(x)
# inner()