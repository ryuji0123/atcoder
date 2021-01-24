def solve():
    ret = 0
    price_per_two = min([8 * Q, 4 * H, 2 * S, D])
    d, m = divmod(N, 2)
    ret += d * price_per_two
    print(ret + (m == 1) * min([4 * Q, 2 * H, S]))


Q, H, S, D = map(int, input().split())
N = int(input())
solve()
