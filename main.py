class Currency:
    currencies = {
        'CHF': 0.930023, # swiss franc
        'CAD': 1.264553, # canadian dollar
        'GBP': 0.737414, # british pound
        'JPY': 111.019919, # japanese yen
        'EUR': 0.862361, # euro
        'USD': 1.0 # us dollar
    }

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit

    def __repr__(self):
        return f"{round(self.value, 2)} {self.unit}"

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        if isinstance(other, Currency):
            other_in_self_unit = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
            return Currency(self.value + other_in_self_unit, self.unit)
        elif isinstance(other, (int, float)):
            return Currency(self.value + other / Currency.currencies[self.unit], self.unit)
        else:
            raise TypeError("Unsupported type for addition with Currency")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Currency):
            other_in_self_unit = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
            return Currency(self.value - other_in_self_unit, self.unit)
        elif isinstance(other, (int, float)):
            return Currency(self.value - other / Currency.currencies[self.unit], self.unit)
        else:
            raise TypeError("Unsupported type for subtraction with Currency")

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Currency(other / Currency.currencies[self.unit] - self.value, self.unit)
        else:
            raise TypeError("Unsupported type for right-side subtraction with Currency")

# Example Usage
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)  # Adds v1 and v2
print(v2 + v1)  # Adds v2 and v1
print(v1 + 3)   # Adds 3 USD to v1
print(3 + v1)   # Adds v1 to 3 USD
print(v1 - 3)   # Subtracts 3 USD from v1
print(30 - v2)  # Subtracts v2 from 30 USD
