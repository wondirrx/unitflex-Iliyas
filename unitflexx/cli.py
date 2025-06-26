import sys
from unitflexx.core import convert

def main():
    if len(sys.argv) != 5:
        print("Usage: cli.py <domain> <from_unit> <to_unit> <value>")
        sys.exit(1)
    
    _, domain, from_unit, to_unit, value_str = sys.argv
    
    try:
        value = float(value_str)
    except ValueError:
        print("Error: Value must be a number")
        sys.exit(1)
    
    try:
        result = convert(domain, from_unit, to_unit, value)
        print(f"{value} {from_unit} = {result:.2f} {to_unit}")
    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()