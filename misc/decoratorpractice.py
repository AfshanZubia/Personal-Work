#decoratorpractice.py
import random
import time
import logging
logger = logging.getLogger(__name__)

'''
In this class, a decorator class that measures the time it takes for a program oto run is created and initalized. The decorator function is applied on three sample methods and the results are displayed.
'''


def time_decorator(func):
	def wrapper(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		end_time = time.time()
		runtime = end_time - start_time
		print(f"Time it took to run: {runtime} seconds.")
		return result
	return wrapper

@time_decorator
def trolley_problem():
	items = ['aliens', 'mothers', 'children', 'dogs', 'cats', 'pigeons', 'people']
	str = f"You have two tracks and a full-speed trolley. On the main track, there are {random.randint(1,20)} {random.choice(items)} tied to the tracks about to get run over. If you pull the lever, the trolley will run over {random.randint(1,20)} {random.choice(items)} instead. Do you pull the lever?"
	return str

@time_decorator
def my_morning_routine():
	str = f"In the morning, I brush my teeth and drink {random.randint(1,20)} cups of coffee."
	return str

@time_decorator
def stock_price():
	price = random.randint(-50000,50000)
	str = f"Today, NVIDIA's stock price is currently ${price}. {'Wow!' if price > 0 else 'Uh oh!'}"
	return str


print(trolley_problem())
print()
print(my_morning_routine())
print()
print(stock_price())
print()
