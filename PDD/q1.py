import sys

def solve(a, b):
    if len(a) <= 1:
        show(a)
        return
    if not b:
        print('NO')
        return
    i = 0
    while i < len(a)-1 and a[i] < a[i+1]:
        i += 1

    if i == len(a)-2:
        _M = max(b)
        if _M > a[i]:
            a[-1] = _M
            show(a)
        else:
            print('NO')
    elif a[i] < a[i+2]:
        m = a[i]
        M = a[i+2]
        _M = min(b)
        for x in b:
            if _M <= x < M:
                _M = x
        if _M > m:
            a[i+1] = _M
            show(a)
        else:
            print('NO')
    else:

        if i == 0:
            _M = min(b)
            for x in b:
                if x < a[i+1] and x > _M:
                    _M = x
            if _M < a[i+1]:
                a[i] = _M
                show(a)
            else:
                print('NO')
        else:
            m = a[i-1]
            _M = min(b)
            for x in b:
                if m < x < a[i+1] and x > _M:
                    _M = x
            if m < _M < a[i+1]:
                a[i] = _M
                show(a)
            else:
                print('NO')
def show(a):
    print(' '.join(map(str, a)))
inps = []
for i, line in enumerate(sys.stdin):
    inps.append(list(map(int, line.strip().split())))
    if i == 1:
        break
solve(inps[0], inps[1])

