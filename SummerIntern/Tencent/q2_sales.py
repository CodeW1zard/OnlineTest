import sys


def sol(a):
    cost = 0
    curr = 0
    for i in range(len(a)):
        demand = a[i]
        curr += demand
        cost += abs(curr)
    print(cost)


if __name__ == '__main__':
    N = sys.stdin.readline()
    a = list(map(int, sys.stdin.readline().strip().split()))
    sol(a)
