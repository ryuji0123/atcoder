from collections import Counter


LIM = pow(10, 5) + 1

def solve():
    counter = Counter(A)
    print(max([sum([counter[i + j] for j in range(3)]) for i in range(LIM)]))


N = int(input())
A = list(map(int, input().split()))
solve()
