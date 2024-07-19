import time
import functools

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		begin = time.time()
		func(*args, **kwargs)
		stop = time.time()
		delta = stop - begin
		print(f"{func.__name__} took {delta:.4f} seconds")
	return wrapper

@speed_calc_decorator
def fast_function():
	for i in range(1000000):
		i * i

@speed_calc_decorator
def slow_function():
	for i in range(10000000):
		i * i


def logging_decorator(fn):
  def wrapper(*args):
    print(f"You called {fn.__name__}{args}")
    result = fn(args[0], args[1], args[2])
    print(f"It returned: {result}")
  return wrapper

@logging_decorator
def a_function(a, b, c):
  return a * b * c

		
if __name__ == "__main__":
	fast_function()
	slow_function()
	
	inputs = eval(input())  # eval() creates list for inputs with format: [1,2,3]
	a_function(inputs[0], inputs[1], inputs[2])
	