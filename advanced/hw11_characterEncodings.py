# Homework 11 - Character Encodings
# This program expects as arguments any number of pathnames of UTF-8 encoded files, 
# and indicates the mean number of bytes per character in the content of each one.
# CS 231 - Advanced Python

import sys
import os
from typing import Union

def mean_bytes_per_character(file_path: str) -> Union[float, str]:
    """
    Calculate the mean number of bytes per character in a UTF-8 encoded file.

    :param file_path: Path to the file.
    :return: Mean bytes per character or error message.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            byte_count = os.path.getsize(file_path)
            char_count = len(content)
            return byte_count / char_count if char_count else 0
    except Exception as e:
        return f"Error processing file {file_path}: {e}"

def main():
    for file_path in sys.argv[1:]:
        result = mean_bytes_per_character(file_path)
        print(f"Mean bytes per character in '{file_path}': {result}")

if __name__ == "__main__":
    main()
