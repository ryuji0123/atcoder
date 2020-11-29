def solve():
    b = [0] * N
    l = 0
    r = N - 1
    diff = 0
    while l <= r:
        if diff % 2 == 0:
            b[l] = a[N - 1 - diff]
            l += 1
        else:
            b[r] = a[N - 1 - diff]
            r -= 1
        diff += 1
    print(*b)


N = int(input())
a = list(map(int, input().split()))
solve()
