from collections import deque


def solve():
    stack = deque()
    for c in S:
        if len(stack) == 0 or stack[-1] != c:
            stack.append(c)
    print(len(stack)) 


N = input()
S = input()
solve()
