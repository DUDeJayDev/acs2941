# Checks if a dividend can be divided by a divisor without a remainder
# (considering edge cases of 0 divisor and negative dividends).


def can_be_divided(dividend, divisor):
    if divisor == 0:
        return False
    elif dividend < 0:
        return can_be_divided(abs(dividend), -divisor)
    else:
        return dividend % divisor == 0


print(can_be_divided(10, 2))
print(can_be_divided(10, 0))
print(can_be_divided(-10, 2))
print(can_be_divided(10, -5))
