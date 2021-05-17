class Solution:
    def divide(self, dividend: int, divisor: int):
        less_than_0 = None
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            less_than_0 = True
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = -1
        while dividend > 0:
            dividend -= divisor
            result += 1

        if less_than_0:
            result *= -1

        return result
