from fractions import Fraction

value1 = Fraction("0.3") - Fraction("0.2")
value2 = Fraction(3, 10) - Fraction(2, 10)
value3 = Fraction("3/10") - Fraction("2/10")

print(value1)
print(float(value1))
print(value2)
print(float(value2))
print(value3)
print(float(value3))