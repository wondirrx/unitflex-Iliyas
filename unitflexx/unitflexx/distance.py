def convert_distance(from_unit: str, to_unit: str, value: float) -> float:
    if from_unit == "kilometers" and to_unit == "miles":
        return round(value * 0.621371, 4)
    elif from_unit == "miles" and to_unit == "kilometers":
        return round(value / 0.621371, 4)
    raise ValueError(f"Unsupported units: {from_unit} to {to_unit}")