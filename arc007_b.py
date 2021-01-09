def solve():
    cases = list(range(N + 1))
    positions = list(range(N + 1))
    cur = 0
    for d in disks:
        if d == cur:
            continue
        cases[positions[d]] = cur
        positions[cur] = positions[d]
        cur = d
    for d in cases[1: ]:
        print(d)

N, M = map(int, input().split())
disks = [int(input()) for _ in range(M)]
solve()
