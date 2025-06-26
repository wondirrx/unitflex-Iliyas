import pytest
from unitflexx.currency import convert_currency

def test_usd_to_eur():
    assert round(convert_currency("usd", "eur", 1), 4) == 0.9
    assert round(convert_currency("usd", "eur", 100), 4) == 90.0
    assert round(convert_currency("usd", "eur", 0.5), 4) == 0.45

def test_eur_to_usd():
    assert round(convert_currency("eur", "usd", 1), 4) == 1.1111
    assert round(convert_currency("eur", "usd", 100), 4) == 111.1111
    assert round(convert_currency("eur", "usd", 0.5), 4) == 0.5556

def test_invalid_currency_units():
    with pytest.raises(ValueError):
        convert_currency("gbp", "usd", 100)
    with pytest.raises(ValueError):
        convert_currency("usd", "jpy", 50)