import pytest
from unitflexx.temperature import convert_temperature

def test_celsius_to_fahrenheit():
    assert round(convert_temperature("celsius", "fahrenheit", 0), 2) == 32.0
    assert round(convert_temperature("celsius", "fahrenheit", 100), 2) == 212.0
    assert round(convert_temperature("celsius", "fahrenheit", -40), 2) == -40.0

def test_fahrenheit_to_celsius():
    assert round(convert_temperature("fahrenheit", "celsius", 32), 2) == 0.0
    assert round(convert_temperature("fahrenheit", "celsius", 212), 2) == 100.0
    assert round(convert_temperature("fahrenheit", "celsius", -40), 2) == -40.0

def test_invalid_temperature_units():
    with pytest.raises(ValueError):
        convert_temperature("kelvin", "celsius", 0)
    with pytest.raises(ValueError):
        convert_temperature("celsius", "kelvin", 100)