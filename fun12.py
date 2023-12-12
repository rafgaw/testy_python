import time
import numpy as np



def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper
@measure_time
def my_function():
    # pass
    total = sum(range(15_000_000))

@measure_time
def my_function2():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print("Suma to: ", suma)

@measure_time
def my_function_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print("Suma w np to: ", total)

my_function()
my_function2()
my_function_np()