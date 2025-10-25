import multiprocessing
import time
import math


def square_sum(start, end):
    return sum(i * i for i in range(start, end + 1))


def worker(args):
    start, end = args
    return square_sum(start, end)


def parallel_calc(N, procs):
    chunk = math.ceil(N / procs)
    ranges = []

    for i in range(procs):
        s = i * chunk + 1
        e = min((i + 1) * chunk, N)
        if s <= N:
            ranges.append((s, e))

    with multiprocessing.Pool(procs) as pool:
        results = pool.map(worker, ranges)

    return sum(results)


def sequential_calc(N):
    return sum(i * i for i in range(1, N + 1))


def main():
    N = 100
    procs = multiprocessing.cpu_count()

    print(f"Calculating sum of squares for N = {N}")
    print(f"Using {procs} processes")

 
    start_parallel = time.time()
    parallel_result = parallel_calc(N, procs)
    end_parallel = time.time()
    parallel_time = end_parallel - start_parallel

    
    start_sequential = time.time()
    sequential_result = sequential_calc(N)
    end_sequential = time.time()
    sequential_time = end_sequential - start_sequential

    print(f"1² + 2² + ... + {N}² = {parallel_result}")
    print(f"Parallel time: {parallel_time:.4f} seconds")
    print(f"Sequential time: {sequential_time:.4f} seconds")


if __name__ == "__main__":
    main()
