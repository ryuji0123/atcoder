def solve():
    ml, mr = 0, float('inf')
    for (l, r) in zip(L, R):
        ml = max(ml, l)
        mr = min(mr, r)
    print(mr - ml + 1 if ml <= mr else 0)


N, M = map(int, input().split())
L = []
R = []
for _ in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
solve()
