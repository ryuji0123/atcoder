def solve():
    n = 1
    while n * (n + 1) // 2 < X:
        n += 1
    print(n)


X = int(input())
solve()
