#!/usr/bin/env python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it into a JSON file.

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if successful, False if the file was not found.
    """
    try:
        data = []
        # Open CSV file and use DictReader to convert rows to dictionaries
        with open(csv_filename, mode='r', encoding='utf-8') as csv_f:
            csv_reader = csv.DictReader(csv_f)
            for row in csv_reader:
                data.append(row)

        # Write the list of dictionaries to data.json
        with open('data.json', mode='w', encoding='utf-8') as json_f:
            json.dump(data, json_f)

        return True
    except FileNotFoundError:
        return False
