import logging
logging.basicConfig(filename='new.log', level=logging.INFO)


# def logger(func):
# 	def log_func(*args):
# 		logging.info(f"Running '{func.__name__}' with arguments: {args} ")
# 		print(func(*args))
# 	return log_func

# @logger
# def add(x, y):
# 	return x + y


# def sub(x, y):
# 	return x - y

# add(12,2)

# add_log = logger(add)
# sub_log = logger(sub)

# sub_log(5,1)

# print(add(9,7))