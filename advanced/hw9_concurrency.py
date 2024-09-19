# Homework 9 - Concurrency
# This program expects pathnames as arguments and creates a pool of workers 
# to all at once count how many lines long each file is.
# CS 231 - Advanced Python

import sys
import concurrent.futures
import argparse
from typing import Tuple, Union

def count_lines(file_path: str) -> Tuple[str, Union[int, str]]:
    """
    Count the number of lines in a file.

    :param file_path: Path to the file.
    :return: Tuple containing file path and line count or error message.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file_path, sum(1 for _ in file)
    except Exception as e:
        return file_path, f"Error: {e}"

def main(args):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(count_lines, args.files)

        for file_path, line_count in results:
            print(f"{file_path}: {line_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count lines in multiple files concurrently.")
    parser.add_argument('files', nargs='+', help='File paths to process')
    args = parser.parse_args()
    main(args)
