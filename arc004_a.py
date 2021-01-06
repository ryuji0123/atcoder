from math import sqrt


def solve():
    print(sorted([sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) for i in range(N) for j in range(i + 1, N)])[-1])


N = int(input())
x, y = [], []
for _ in range(N):
    tmp = list(map(int, input().split()))
    x.append(tmp[0])
    y.append(tmp[1])
solve()
