from collections import Counter


def solve():
    counter = Counter(A)
    for i in range(1, N + 1):
        print('Yes' if Q - counter[i] < K else 'No')


N, K, Q = map(int, input().split())
A = []
for _ in range(Q):
    A.append(int(input()))
solve()
