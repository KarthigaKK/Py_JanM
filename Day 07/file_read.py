# f = open('demo.txt', 'r')

# print(f.read())



# f.close()

# print(f.closed)


# with open('demo.txt', 'r') as f:

# 	for line in f:
# 		print(line, end='')
	
	# f_content = f.readline()
	# print(f_content, end='')

	# f_content = f.readline()
	# print(f_content, end='')

	# f_content = f.readline()
	# print(f_content, end='')


# with open('demo_1.txt', 'w') as f:
# 	f.write('Demo')
# 	f.seek(0)
# 	f.write('Newline')


with open('demo.txt', 'r') as rf:
	with open('demo_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)

# with open('screenshot.jpg', 'rb') as rf:
	# with open('screenshot_copy.jpg', 'wb') as wf:
		# for line in rf:
			# wf.write(line)


ctrl + shift + /