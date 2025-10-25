import multiprocessing
import time


def calculate_factorial(number):
    factorial_result = 1
    for current in range(1, number + 1):
        factorial_result *= current
    print(f"Factorial of {number} is {factorial_result}")
    return factorial_result


def sequential_calculations(values):
    for value in values:
        calculate_factorial(value)


def execute_calculations():
    values = [5, 10, 15, 20, 25]

    print("Beginning factorial computations...")


    print("--- Parallel Execution ---")
    start_parallel = time.time()

    calculation_processes = []
    for value in values:
        process = multiprocessing.Process(target=calculate_factorial, args=(value,))
        calculation_processes.append(process)
        process.start()

    for process in calculation_processes:
        process.join()

    end_parallel = time.time()
    parallel_time = end_parallel - start_parallel


    print("\n--- Sequential Execution ---")
    start_sequential = time.time()
    sequential_calculations(values)
    end_sequential = time.time()
    sequential_time = end_sequential - start_sequential

    print(f"\nParallel time: {parallel_time:.4f} seconds")
    print(f"Sequential time: {sequential_time:.4f} seconds")


if __name__ == "__main__":
    execute_calculations()
