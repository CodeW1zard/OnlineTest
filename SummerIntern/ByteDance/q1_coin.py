'''
找零
'''
import sys

coins = [64, 16, 4, 1]


def sol(v):
    n = 0
    for coin in coins:
        d, v = v // coin, v % coin
        n += d
    return n


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    print(sol(1024 - N))
