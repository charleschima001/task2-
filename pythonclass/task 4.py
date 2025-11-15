import multiprocessing
import time

def calculate_factorial(number):
    factorial_result = 1
    for current in range(1, number + 1):
        factorial_result *= current
    print(f"Factorial of {number} is calculated")
    return factorial_result

def sequential_calculations(values):
    for value in values:
        calculate_factorial(value)

def execute_calculations():

    values = [50000, 50000, 50000, 50000, 50000]  
    
    print("Beginning factorial computations...")

    print("--- Sequential Execution ---")
    start_sequential = time.time()
    sequential_calculations(values)
    end_sequential = time.time()
    sequential_time = end_sequential - start_sequential

    print("\n--- Parallel Execution ---")
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

    print(f"\nSequential time: {sequential_time:.4f} seconds")
    print(f"Parallel time: {parallel_time:.4f} seconds")
    print(f"Speedup: {sequential_time/parallel_time:.2f}x")

if __name__ == "__main__":
    execute_calculations()
