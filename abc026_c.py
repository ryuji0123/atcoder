def solve():
    def dfs(root):
        if len(children[root]) == 0:
            return 1
        vals = [dfs(node) for node in children[root]]
        return max(vals) + min(vals) + 1
    print(dfs(1))

N = int(input())
children = {i: [] for i in range(1, N + 1)}
for i in range(N - 1):
    b = int(input())
    children[b].append(i + 2)
solve()
