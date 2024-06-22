import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


def speed_calc_decorator(function):
    def run_time():
        start_time = current_time
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return run_time


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
