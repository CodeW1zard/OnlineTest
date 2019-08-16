import sys

def timeint(h, m):
    return h * 60 + m

def inttime(t):
    h, m = t//60, t%60
    return "%d %d"%(h, m)

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    ts = []
    for i in range(N):
        h, m = sys.stdin.readline().strip().split()
        ts.append(timeint(int(h), int(m)))
    dist = int(sys.stdin.readline().strip())
    H, M = sys.stdin.readline().strip().split()
    ddl = timeint(int(H), int(M)) - dist

    best = -1
    for t in ts:
        if t <= ddl and t > best:
            best = t
    print(inttime(best))


