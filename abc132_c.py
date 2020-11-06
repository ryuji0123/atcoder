def solve():
    if N % 2 == 1:
        print(0)
        return
    d.sort()
    print(d[N // 2] - d[N // 2 - 1])


N = int(input())
d = list(map(int, input().split()))
solve()
