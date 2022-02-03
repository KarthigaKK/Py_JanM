# try:
# 	pass
# except Exception:
# 	pass
# else:
# 	pass
# finally:
# 	pass

"""
 Hello


"""

"""
FileNotFoundError
NameError
"""


try:
	f = open('test_file.txt', 'r')
	# old_var = new_var

except FileNotFoundError as e:
	print(e)

except NameError as e:
	print(e)

except Exception as e:
	print(e)

else:
	print(f.read())
	f.close()
finally:
	print('Executing......')



# f = open('testfile.txt', 'r')