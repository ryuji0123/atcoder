from collections import Counter
from math import sqrt


MOD = pow(10, 9) + 7


def factorization(n):
    arr = []
    tmp = n
    div = 2
    while div * div <= n:
        if tmp % div == 0:
            cnt = 0
            while tmp % div == 0:
                cnt += 1
                tmp //= div
            arr.append([div, cnt])
        div += 1

    if tmp != 1:
        arr.append([tmp, 1])

    if len(arr) == 0:
        arr.append([n, 1])

    return arr


def solve():
    if N == 1:
        print(1)
        return

    counter = Counter()
    for n in range(2, N + 1):
        for e, c in factorization(n):
            counter[e] += c
    ret = 1
    for e, c in counter.items():
        ret *= c + 1
        ret %= MOD
    print(ret)


N = int(input())
solve()
