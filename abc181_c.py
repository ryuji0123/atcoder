def solve():
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if (y[k] - y[i]) * (x[j] - x[i]) == (y[j] - y[i]) * (x[k] - x[i]):
                    print('Yes')
                    return
    print('No')

N = int(input())
x, y = [], []
for _ in range(N):
    tmp = list(map(int, input().split()))
    x.append(tmp[0])
    y.append(tmp[1])
solve()
