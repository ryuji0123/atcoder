from itertools import accumulate


def solve():
    acc_sum = list(accumulate(a))
    print(min([abs(acc_sum[-1] - 2 * acc_sum[idx]) for idx in range(N - 1)]))


N = int(input())
a = list(map(int, input().split()))
solve()
