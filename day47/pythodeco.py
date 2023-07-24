import time


def speed_calculator_decorator(function):
    def wrapper():
        startTime = time.time()
        function()
        endTime = time.time()
        print(f"{function.__name__} rund for : {endTime - startTime}s")

    return wrapper


@speed_calculator_decorator
def fast_func():
    for i in range(1000000):
        i * i


@speed_calculator_decorator
def slow_func():
    for i in range(10000000):
        i * i

fast_func()
slow_func()
