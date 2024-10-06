from test_framework import generic_test


def swap_bits(x, i, j):
    '''
    If the bits at the ith and jth positions are different, flip them separately using XOR (^)
    '''
    if x >> i & 1 != x >> j & 1:
        mask = 1 << i | 1 << j
        x ^= mask
    return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
