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


def main():

    N = 100
    procs = multiprocessing.cpu_count()

    print(f"Calculating sum of squares for N = {N}")
    print(f"Using {procs} processes")

    start = time.time()
    result = parallel_calc(N, procs)
    end = time.time()

    print(f"1² + 2² + ... + {N}² = {result}")
    print(f"Time taken: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()