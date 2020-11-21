TO, CAP, REV = 0, 1, 2
INF = float('inf')

class FordFulkerson:
 
    def __init__(self, N):
        self.N = N
        self.G = [[] for _ in range(N)]
        self.used = [False] * N

    def addEdge(self, from_, to_, capacity):
        self.G[from_].append([to_, capacity, len(self.G[to_])])
        self.G[to_].append([from_, 0, len(self.G[from_]) - 1])

    def dfs(self, v, t, f):
        if v == t:
            return f

        self.used[v] = True
        for e in self.G[v]:
            if self.used[e[TO]] or e[CAP] <= 0:
                continue

            d = self.dfs(e[TO], t, min(f, e[CAP]))
            if d <= 0:
                continue

            e[CAP] -= d
            self.G[e[TO]][e[REV]][CAP] += d
            return d

        return 0

    def maxFlow(self, s, t):
        flow = 0
        while True:
            for i in range(self.N):
                self.used[i] = False
            f = self.dfs(s, t, INF)
            if f == 0:
                return flow
            flow += f


def solve():
    ff = FordFulkerson(2 * N + 2)
    s = 2 * N
    t = s + 1
    for i in range(N):
        ff.addEdge(s, i, 1)
        ff.addEdge(N + i, t, 1)

    for i, r in enumerate(red):
        for j, b in enumerate(blue):
            if r[0] < b[0] and r[1] < b[1]:
                ff.addEdge(i, N + j, 1)

    print(ff.maxFlow(s, t))


N = int(input())
red = []
for _ in range(N):
    red.append(list(map(int, input().split())))
blue = []
for _ in range(N):
    blue.append(list(map(int, input().split())))
solve()
