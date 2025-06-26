import urllib.request
import json

RATE_USD_TO_EUR = 0.9

def _get_live_rate(from_currency: str, to_currency: str) -> float:
    url = f"https://api.exchangerate.host/convert?from=USD&to=EUR"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            if response.status != 200:
                return None
            data = json.loads(response.read().decode())
            if data.get('success', False):
                return data['result']
    except Exception:
        pass
    return None

def convert_currency(from_unit: str, to_unit: str, value: float) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if (from_unit, to_unit) == ("usd", "eur"):
        rate = _get_live_rate("USD", "EUR")
        if rate is None:
            rate = RATE_USD_TO_EUR
        return value * rate
    elif (from_unit, to_unit) == ("eur", "usd"):
        rate = _get_live_rate("EUR", "USD")
        if rate is None:
            rate = 1 / RATE_USD_TO_EUR
        return value * rate
    else:
        raise ValueError(f"Unsupported currency units: {from_unit} to {to_unit}")