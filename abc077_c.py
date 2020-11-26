# time: O(NlogN)
# soace: O(N)

import bisect

from itertools import accumulate


def solve():
    acc_sum = list(accumulate(
        [0] + [N - bisect.bisect_right(C, b) for b in reversed(B)]
        ))[::-1]
    print(sum([acc_sum[bisect.bisect_right(B, a)] for a in A]))


N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
solve()
