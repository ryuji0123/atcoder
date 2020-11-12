# time: O(N^2)
# space: O(1)

def solve():
    ret = 0
    while sum(h):
        l = 0
        while l < len(h) - 1 and h[l] == 0:
            l += 1
        m = h[l]
        r = l
        while r < len(h) and h[r] != 0:
            m = min(m, h[r])
            r += 1
        for i in range(l, r):
            h[i] -= m
        ret += m
    print(ret)


N = int(input())
h = list(map(int, input().split()))
solve()
