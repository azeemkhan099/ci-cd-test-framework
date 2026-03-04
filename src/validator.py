# src/validator.py
import json
import os

def load_data(path):
    with open(path, "r") as f:
        return json.load(f)

def run_validations(input_data):
    # 1) Normalize input into "data"
    if isinstance(input_data, list):
        data = input_data

    elif isinstance(input_data, str):
        if os.path.exists(input_data):
            data = load_data(input_data)
        else:
            raise ValueError("Invalid input: file path does not exist")

    else:
        raise ValueError("Invalid input: must be list or valid file path")

    # 2) Optional: unwrap {"data": [...]} shape
    if isinstance(data, dict) and "data" in data:
        data = data["data"]

    # 3) Ensure i have a list
    if not isinstance(data, list):
        raise ValueError("Invalid data format: expected a list")

    # 4) Validate list content
    if not data:
        return "No data"

    for idx, item in enumerate(data):
        if item is None:
            return "Invalid data"
        if isinstance(item, bool) or not isinstance(item, int):
            return "Invalid data"
        if item < 0:
            return "Invalid data"

    return "Valid data"