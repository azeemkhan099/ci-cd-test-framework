# tests/test_validator_extra.py
from src.validator import run_validations

def test_all_none():
    assert run_validations([None, None]) == "Invalid data"

def test_mixed_data():
    assert run_validations([1, None, 3]) == "Invalid data"

def test_large_list():
    assert run_validations(list(range(1000))) == "Valid data"
