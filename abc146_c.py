def solve():
    ret = 0
    left, right = 0, pow(10, 9) + 1
    while left < right:
        mid = left + right >> 1
        d = 1
        tmp = mid
        while tmp // 10:
            tmp //= 10
            d += 1
        price = A * mid + B * d
        if price <= X:
            ret = max(ret, mid)
            left = mid + 1
        else:
            right = mid
    print(ret)

A, B, X = map(int, input().split())
solve()
