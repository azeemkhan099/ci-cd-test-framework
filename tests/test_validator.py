from src.validator import run_validations

def test_validation():
    results = run_validations("tests/sample_data.json")
    assert results["temperature_check"] is True
    assert results["pressure_check"] is True
