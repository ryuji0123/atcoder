def solve():
    ret = i = 0
    while i + 1 < N:
        i += 1
        cur = 0
        while i < N and H[i] <= H[i - 1]:
            cur += 1
            i += 1
        ret = max(ret, cur)
    print(ret)


N = int(input())
H = list(map(int, input().split()))
solve()
