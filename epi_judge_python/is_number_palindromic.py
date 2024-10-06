from test_framework import generic_test
import math

def is_palindrome_number(x: int) -> bool:
    # edge cases
    if x < 0: return False
    if x < 10: return True

    div = pow(10, int(math.log10(x)))
    while x > 0:
        # compare first and last digits
        first_digit = x // div
        last_digit = x % 10
        if first_digit != last_digit: return False

        # remove first and last digits
        x %= div
        x //= 10
        div //= 100

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
