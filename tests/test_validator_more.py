import json
import pytest
from pathlib import Path

from src.validator import run_validations

def test_empty_list_returns_no_data():
    assert run_validations([]) == "No data"

def test_invalid_input_type_raises_value_error():
    with pytest.raises(ValueError):
        run_validations(123)

def test_nonexistent_path_raises_value_error():
    with pytest.raises(ValueError):
        run_validations("tests/does_not_exist.json")

def test_json_file_empty_list_returns_no_data(tmp_path):
    p = tmp_path / "empty.json"
    p.write_text("[]")
    assert run_validations(str(p)) == "No data"

def test_json_file_with_null_is_invalid(tmp_path):
    p = tmp_path / "has_null.json"
    p.write_text("[null]")
    assert run_validations(str(p)) == "Invalid data"

def test_broken_json_raises_decode_error(tmp_path):
    p = tmp_path / "broken.json"
    p.write_text("{not valid json")
    with pytest.raises(json.JSONDecodeError):
        run_validations(str(p))
