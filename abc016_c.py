def solve():
    for root in range(1, N + 1):
        tmp = set()
        for node in adj[root]:
            for friend in adj[node]:
                if friend == root or friend in adj[root]:
                    continue
                tmp.add(friend)
        print(len(tmp))


N, M = map(int, input().split())
adj = {k: [] for k in range(1, N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
solve()
