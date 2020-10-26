def solve():
    m_cost = float('inf')
    for i in range(pow(2, N)):
        skills = [0] * M
        cost = 0
        for j in range(N):
            if not (i >> j & 1):
                continue
            for m in range(M):
                skills[m] += A[j][m]
            cost += C[j]
        if all([X <= s for s in skills]):
            m_cost = min(m_cost, cost)
    print(m_cost if m_cost < float('inf') else -1)
        

N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    C.append(tmp[0])
    A.append(tmp[1: ])
solve()
