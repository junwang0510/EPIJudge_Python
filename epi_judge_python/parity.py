from test_framework import generic_test


def parity(x: int) -> int:
    '''
    x & x - 1 removes the least significant set bit
    '''
    count = 0
    while x:
        x &= x - 1
        count += 1
    return count % 2


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
