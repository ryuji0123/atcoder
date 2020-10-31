def solve():
    accepted = {}
    wa_counter = {}
    penalty = 0
    for p, s in zip(P, S):
        if p in accepted:
            continue
        if s == 'WA':
            wa_counter[p] = wa_counter.get(p, 0) + 1
        else:
            penalty += wa_counter.get(p, 0)
            accepted[p] = True
    print(len(accepted), penalty)


N, M = map(int, input().split())
P, S = [], []
for _ in range(M):
    p, s = input().split()
    P.append(p)
    S.append(s)
solve()
