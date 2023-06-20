class ProperFraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return ProperFraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return ProperFraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return ProperFraction(numerator, denominator)


fraction1 = ProperFraction(1, 2)
fraction2 = ProperFraction(3, 4)

print(fraction1 == fraction2)  # Виводить: False
print(fraction1 < fraction2)  # Виводить: True
print(fraction1 > fraction2)  # Виводить: False

fraction3 = fraction1 + fraction2
print(fraction3)  # Виводить: 5/4

fraction4 = fraction1 - fraction2
print(fraction4)  # Виводить: -1/4

fraction5 = fraction1 * fraction2
print(fraction5)  # Виводить: 3/8
