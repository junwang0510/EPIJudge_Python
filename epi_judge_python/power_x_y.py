from test_framework import generic_test


def power(x: float, y: int) -> float:
    if y == 0:
        return 1
    if x == 0:
        return 0
    if y < 0:
        x = 1 / x
        y = -y

    res = 1
    while y > 0:
        if y % 2:
            res *= x
        x **= 2
        y //= 2
    return res

if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
