def convert_temperature(from_unit: str, to_unit: str, value: float) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    raise ValueError(f"Unsupported units: {from_unit} to {to_unit}")