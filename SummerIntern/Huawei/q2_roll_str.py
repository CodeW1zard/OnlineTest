import sys
import re


def solve2(s):
    stack_s = []
    stack_b = []
    rights = [")", "]", "}"]
    i = 0
    n = len(s)
    res = ""
    while i < n:
        prev = i
        c = s[i]
        if is_number(s[i]):
            while i < n and is_number(s[i]):
                i += 1
            stack_b.append(int(s[prev:i]))
            i += 1  # 括号
            prev = i
            while i < n and is_alpha(s[i]):
                i += 1
            stack_s.append(s[prev:i])

        elif is_alpha(s[i]):
            while i < n and is_alpha(s[i]):
                i += 1
            if not stack_b:
                res += s[prev:i]
            else:
                stack_s[-1] += s[prev:i]

        elif s[i] in rights:
            b = stack_b.pop()
            c = stack_s.pop()
            tmp = b * c
            if stack_s:
                stack_s[-1] += tmp
            if not stack_b:
                res += tmp
            i += 1
        else:
            i += 1
    while len(stack_b) != 0:
        res += stack_s.pop() * stack_b.pop()
    print(res)
    print(res[::-1])


def is_alpha(c):
    return re.match("[a-zA-Z]", c) is not None


def is_number(c):
    return re.match("[0-9]", c) is not None


if __name__ == '__main__':
    inputs = sys.stdin.readline().strip()
    solve2(inputs)
