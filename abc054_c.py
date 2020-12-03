from collections import defaultdict


def solve():
    def dfs(root, count):
        if count == N:
            ret[0] += 1
            return

        for node in adj[root]:
            if not seen[node]:
                seen[node] = True
                
                dfs(node, count + 1)
                
                seen[node] = False

    seen = {node: False for node in range(1, N + 1)}
    seen[1] = True
    ret = [0]
    dfs(1, 1)
    print(ret[0])


N, M = map(int, input().split())
adj = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
solve()
