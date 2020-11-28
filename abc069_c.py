from collections import Counter


MOD = 4


def solve():
    counter = Counter([a % MOD for a in A])
    if (counter[1] + counter[3] <= counter[0]) or (counter[1] + counter[3] - 1 == counter[0] and counter[2] == 0):
        print('Yes')
    else:
        print('No')


N = input()
A = list(map(int, input().split()))
solve()
