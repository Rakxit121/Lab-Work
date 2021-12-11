# Given a positive real number, print its fractional part.
import math

a = 133.5
y, x = math.modf(a)
print(y)
print(x)
