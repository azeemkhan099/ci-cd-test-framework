import json

def load_data(path):
    with open(path, "r") as f:
        return json.load(f)

def validate_temperature(data):
    return all(15 <= x <= 30 for x in data["temperature"])

def validate_pressure(data):
    return all(0.9 <= x <= 1.1 for x in data["pressure"])

def run_validations(path):
    data = load_data(path)
    results = {
        "temperature_check": validate_temperature(data),
        "pressure_check": validate_pressure(data),
    }
    return results
