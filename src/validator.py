# src/validator.py
import json
import os

def load_data(path):
    with open(path, "r") as f:
        return json.load(f)

def run_validations(input_data):
    if isinstance(input_data, list):
        data = input_data
    elif isinstance(input_data, str) and os.path.exists(input_data):
        data = load_data(input_data)
    else:
        raise ValueError("Invalid input: must be list or valid file path")

    if not data:
        return "No data"
    for item in data:
        if item is None:
            return "Invalid data"
    return "Valid data"
