from test_framework import generic_test


def divide(x: int, y: int) -> int:
    quotient = 0
    for i in range(31, -1, -1):
        if (y << i) <= x: # get the maximum (y * 2^k) that is <= x
            x -= (y << i) # x -= y * 2^k
            quotient += (1 << i) # quotient += 2^k (you took 2^k y away from x)
    return quotient

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
