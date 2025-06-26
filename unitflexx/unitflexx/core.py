from .temperature import convert_temperature
from .distance import convert_distance
from .currency import convert_currency

def convert(domain: str, from_unit: str, to_unit: str, value: float) -> float:
    domain = domain.lower()
    if domain == "temperature":
        return convert_temperature(from_unit, to_unit, value)
    elif domain == "distance":
        return convert_distance(from_unit, to_unit, value)
    elif domain == "currency":
        return convert_currency(from_unit, to_unit, value)
    raise ValueError(f"Unsupported domain: {domain}")