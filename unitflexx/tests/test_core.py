import pytest
from unitflexx.core import convert

def test_valid_temperature_conversion():
    assert round(convert("temperature", "celsius", "fahrenheit", 0), 2) == 32.0
    assert round(convert("temperature", "fahrenheit", "celsius", 32), 2) == 0.0

def test_valid_distance_conversion():
    assert round(convert("distance", "kilometers", "miles", 1), 4) == 0.6214
    assert round(convert("distance", "miles", "kilometers", 1), 4) == 1.6093

def test_valid_currency_conversion():
    assert round(convert("currency", "usd", "eur", 1), 4) == 0.9
    assert round(convert("currency", "eur", "usd", 1), 4) == 1.1111

def test_invalid_domain():
    with pytest.raises(ValueError):
        convert("weight", "kg", "lb", 10)
    with pytest.raises(ValueError):
        convert("volume", "liter", "gallon", 5)