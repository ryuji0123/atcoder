def solve():
    ret = 0
    for i in range(pow(2, N)):
        used = [0] * N
        for j in range(N):
            if i >> j & 1:
                used[j] = 1
        ret += all([p[idx] == sum([used[s - 1] for s in S[idx]]) % 2 for idx in range(M)])
    print(ret)


N, M = map(int, input().split())
S = []
for _ in range(M):
    tmp = list(map(int, input().split()))
    S.append(tmp[1: ])
p = list(map(int, input().split()))
solve()
