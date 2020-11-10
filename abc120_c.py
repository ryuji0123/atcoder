from collections import deque


def solve():
    stack = deque()
    for c in S:
        if len(stack) == 0 or stack[-1] == c:
            stack.append(c)
        else:
            stack.pop()
    print(len(S) - len(stack))


S = input()
solve()
