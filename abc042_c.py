from collections import deque


def solve():
    nums = [n for n in range(10) if n not in D]
    stack = deque()
    for n in nums:
        if n == 0:
            continue
        stack.append(n)

    while stack:
        val = stack.popleft()
        if N <= val:
            print(val)
            return
        for n in nums:
            stack.append(10 * val + n)


N, K = map(int, input().split())
D = list(map(int, input().split()))
solve()
