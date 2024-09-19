# Homework 13 - Web Service
# This program is a CSV-to-JSON translator that expects the path to a CSV file as argument, 
# and for each line in the file, prints out a JSON object encapsulating that record.
# CS 231 - Advanced Python


import csv
import json
import argparse
import logging
import sys

def csv_to_json(csv_file_path, output_file=None, delimiter=','):
    """Converts a CSV file to JSON format.

    Args:
        csv_file_path (str): Path to the CSV file.
        output_file (str, optional): Path to save the output JSON file. Prints to console if None.
        delimiter (str, optional): Delimiter used in the CSV file. Defaults to ','.
    """
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=delimiter)
            json_data = [row for row in reader]

            if output_file:
                with open(output_file, 'w', encoding='utf-8') as jsonfile:
                    json.dump(json_data, jsonfile, ensure_ascii=False, indent=4)
            else:
                for item in json_data:
                    print(json.dumps(item, ensure_ascii=False))
    except FileNotFoundError:
        logging.error(f"The file {csv_file_path} was not found.")
    except PermissionError:
        logging.error(f"Permission denied while accessing the file {csv_file_path}.")
    except csv.Error as e:
        logging.error(f"Error processing CSV file: {e}")

def main():
    """Main function to handle argument parsing and invoke CSV to JSON conversion."""
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description="CSV to JSON Translator")
    parser.add_argument('csv_file_path', type=str, help="Path to the CSV file")
    parser.add_argument('-o', '--output', type=str, help="Path to the output JSON file", required=False)
    parser.add_argument('-d', '--delimiter', type=str, default=',', help="Delimiter used in the CSV file", required=False)
    args = parser.parse_args()

    csv_to_json(args.csv_file_path, args.output, args.delimiter)

if __name__ == "__main__":
    main()
