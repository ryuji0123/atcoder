def solve():
    print(sorted([
        a[i] + a[j] + a[k]
        for i in range(5)
        for j in range(i + 1, 5)
        for k in range(j + 1, 5)
    ], reverse=True)[2])


a = list(map(int, input().split()))
solve()
