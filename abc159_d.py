from collections import Counter


def solve():
    counter = Counter(A)
    s = sum([counter[e] * (counter[e] - 1) // 2 for e in counter.keys()])
    for k in range(N):
        num = counter[A[k]]
        print(s + (num - 1) * (num - 2) // 2 - num * (num - 1) // 2)


N = int(input())
A = list(map(int, input().split()))
solve()
