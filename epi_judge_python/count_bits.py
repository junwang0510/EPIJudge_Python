from test_framework import generic_test


def count_bits(x: int) -> int:
    '''
    x & x - 1 removes the least significant set bit
    '''
    count = 0
    while x:
        x &= x - 1
        count += 1
    return count

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
