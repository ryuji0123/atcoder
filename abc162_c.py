# time: O(K^3)
# space: O(1)
from math import gcd


def solve():
    ret = 0
    for a in range(1, K + 1):
        for b in range(1, K + 1):
            tmp_gcd = gcd(a, b)
            for c in range(1, K + 1):
                ret += gcd(tmp_gcd, c)
    print(ret)


K = int(input())
solve()
