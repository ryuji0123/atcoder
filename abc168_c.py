from math import cos, sqrt, radians


def solve():
    t = H + M / 60
    a_dig = t / 12 * 360
    b_dig = t * 360
    diff = min(abs(a_dig - b_dig), 360 - abs(a_dig - b_dig))
    print(sqrt(A**2 + B**2 - 2 * A * B * cos(radians(diff))))

A, B, H, M = map(int, input().split())
solve()
