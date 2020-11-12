def solve():
    h.sort(reverse=True)
    print(min([h[i] - h[i + K - 1] for i in range(N - K + 1)]))


N, K = map(int, input().split())
h = []
for _ in range(N):
    h.append(int(input()))
solve()
