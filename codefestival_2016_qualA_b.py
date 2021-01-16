def solve():
    d = {idx + 1: v for idx, v in enumerate(a)}
    used = set()
    ret = 0
    for idx in range(1, N + 1):
        if idx in used:
            continue
        if idx == d[d[idx]]:
            used.add(d[idx])
            ret += 1
        used.add(idx)
    print(ret)


N = int(input())
a = list(map(int, input().split()))
solve()
