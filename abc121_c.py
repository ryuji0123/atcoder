def solve():
    costs.sort(key=lambda x: x[0])
    ret = idx = 0
    rest = M
    while rest:
        A, B = costs[idx]
        if B < rest:
            ret += A * B
            rest -= B
        else:
            print(ret + A * rest)
            return
        idx += 1


N, M = map(int, input().split())
costs = []
for _ in range(N):
    A, B = map(int, input().split())
    costs.append([A, B])
solve()
