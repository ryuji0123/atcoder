from itertools import accumulate


def solve():
    sa, sb = [0] + list(accumulate(A)), [0] + list(accumulate(B))
    a_num = N
    b_num = 0
    ret = 0
    while 0 <= a_num:
        while b_num < M and sa[a_num] + sb[b_num + 1] <= K:
            b_num += 1
        ret = max(ret, a_num + b_num if sa[a_num] + sb[b_num] <= K else 0)
        a_num -= 1
    print(ret)


N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
solve()
