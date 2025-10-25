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


def process_files():
    file_list = [filename for filename in os.listdir()
                 if os.path.isfile(filename)][:5]

    print(f"Encoding {len(file_list)} files to Base64...")

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=3) as thread_pool:
        encoding_results = list(thread_pool.map(encode_file_to_base64, file_list))

    end_time = time.time()

    for file_path, encoded_data, error_info in encoding_results:
        if error_info:
            print(f" {file_path}: Error - {error_info}")
        else:
            print(f"{file_path}: {len(encoded_data)} characters")

    print(f"All files encoded in {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    process_files()