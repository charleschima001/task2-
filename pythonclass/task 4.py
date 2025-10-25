import multiprocessing
import time


def calculate_factorial(number):
    factorial_result = 1
    for current in range(1, number + 1):
        factorial_result *= current
    print(f"Factorial of {number} is {factorial_result}")
    return factorial_result


def execute_calculations():

    values = [5, 10, 15, 20, 25]

    print("Beginning factorial computations...")
    start_time = time.time()

    calculation_processes = []
    for value in values:
        process = multiprocessing.Process(target=calculate_factorial, args=(value,))
        calculation_processes.append(process)
        process.start()


    for process in calculation_processes:
        process.join()

    end_time = time.time()
    print(f"All calculations completed in {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    execute_calculations()