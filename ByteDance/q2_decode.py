import sys

if __name__ == '__main__':
    N, K = sys.stdin.readline().strip().split()
    N = int(N)
    K = int(K)
    enc = sys.stdin.readline().strip()
    dec = ''
    cum = 0
    i = 0
    while i < N:
        x = (int(enc[i]) + cum) % 2
        dec += str(x)
        i += 1
        if i < K:
            cum += x
        else:
            cum += x - int(dec[i-K])

    print(dec)