from sys import stdin


def solve(rows, cols):
    res = 0
    for x_value, col in cols.items():
        res += col[1] - col[0] + 1
        for y_value, row in rows.items():
            res += row[1] - row[0] + 1
            if x_value <= row[1] & x_value >= row[0] & y_value <= col[1] & y_value >= col[0]:
                res -= 1
    return res


if __name__ == '__main__':
    n = int(stdin.readline().strip())
    rows = {}
    cols = {}
    total = 0
    for _ in range(n):
        x = list(map(int, stdin.readline().strip().split()))
        if x[0] == x[2]:
            if x[1] > x[3]:
                x[1], x[3] = x[3], x[1]
            if x[0] not in cols:
                cols[x[0]] = [x[1], x[3]]
            else:
                if x[1] < cols[x[0]][0]:
                    cols[x[0]][0] = x[1]
                if x[3] > cols[x[0]][1]:
                    cols[x[0]][1] = x[3]

        elif x[1] == x[3]:
            if x[0] > x[2]:
                x[0], x[2] = x[2], x[0]
            if x[1] not in rows:
                rows[x[1]] = [x[0], x[2]]
            else:
                if x[0] < cols[x[0]][0]:
                    cols[x[0]][0] = x[0]
                if x[2] > cols[x[0]][1]:
                    cols[x[0]][1] = x[2]
        else:
            raise ValueError

    print(solve(rows, cols))
