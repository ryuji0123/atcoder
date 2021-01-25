from collections import deque


def solve():
    indices = [0] * 3
    cur = 0
    d = {chr(k): i for i, k in enumerate(range(ord('a'), ord('a') + 3))}
    users = [chr(k) for k in range(ord('A'), ord('D'))]
    while True:
        if len(cards[cur]) == 0:
            print(users[cur])
            return
        cur = d[cards[cur].popleft()]


cards = [deque(input()) for _ in range(3)]
solve()
