from test_framework import generic_test


def multiply(x: int, y: int) -> int:
    def add(x, y):
        while y:
            carry = (x & y) << 1
            x = x ^ y
            y = carry
        return x

    total = 0
    while y:
        if y % 2:
            total = add(total, x)
        x <<= 1
        y >>= 1
    return total

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
