import base64
import os
import time
from concurrent.futures import ThreadPoolExecutor


def encode_file_to_base64(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content).decode('utf-8')
        return (file_path, encoded_content, None)
    except Exception as error:
        return (file_path, None, str(error))


def sequential_encode_files(file_list):
    results = []
    for file_path in file_list:
        results.append(encode_file_to_base64(file_path))
    return results


def process_files():
    file_list = [filename for filename in os.listdir()
                 if os.path.isfile(filename)][:5]

    print(f"Encoding {len(file_list)} files to Base64...")


    print("--- Parallel Execution ---")
    start_parallel = time.time()

    with ThreadPoolExecutor(max_workers=3) as thread_pool:
        encoding_results = list(thread_pool.map(encode_file_to_base64, file_list))

    end_parallel = time.time()
    parallel_time = end_parallel - start_parallel


    for file_path, encoded_data, error_info in encoding_results:
        if error_info:
            print(f" {file_path}: Error - {error_info}")
        else:
            print(f"{file_path}: {len(encoded_data)} characters")


    print("\n--- Sequential Execution ---")
    start_sequential = time.time()
    sequential_results = sequential_encode_files(file_list)
    end_sequential = time.time()
    sequential_time = end_sequential - start_sequential


    for file_path, encoded_data, error_info in sequential_results:
        if error_info:
            print(f" {file_path}: Error - {error_info}")
        else:
            print(f"{file_path}: {len(encoded_data)} characters")

    print(f"\nParallel time: {parallel_time:.4f} seconds")
    print(f"Sequential time: {sequential_time:.4f} seconds")


if __name__ == "__main__":
    process_files()
