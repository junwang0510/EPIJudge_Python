from test_framework import generic_test


def reverse(x: int) -> int:
    is_negative = True if x < 0 else False
    x = abs(x)
    res = 0

    while x:
        res = res * 10 + x % 10
        x //= 10

    return -res if is_negative else res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
