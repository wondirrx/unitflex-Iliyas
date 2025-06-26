import pytest
from unitflexx.distance import convert_distance

def test_kilometers_to_miles():
    assert round(convert_distance("kilometers", "miles", 1), 4) == 0.6214
    assert round(convert_distance("kilometers", "miles", 5), 4) == 3.1069
    assert round(convert_distance("kilometers", "miles", 10), 4) == 6.2137

def test_miles_to_kilometers():
    assert round(convert_distance("miles", "kilometers", 1), 4) == 1.6093
    assert round(convert_distance("miles", "kilometers", 3.1), 4) == 4.989
    assert round(convert_distance("miles", "kilometers", 10), 4) == 16.0934

def test_invalid_distance_units():
    with pytest.raises(ValueError):
        convert_distance("meters", "miles", 1000)
    with pytest.raises(ValueError):
        convert_distance("kilometers", "yards", 5)