# Calc Execution Time

import time


def calc_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        func(*args, **kwargs)

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        print(f"Execution time = {elapsed_time:.1f} seconds")

    return wrapper


@calc_execution_time
def function(greet, name, times=1):
    # Block of code
    for i in range(times):
        print(f"{greet}, {name}!")


function("Hello", "Alice", 10)
