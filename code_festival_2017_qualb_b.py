from collections import Counter


def solve():
    counter = Counter(D)
    for t in T:
        if counter[t] == 0:
            print('NO')
            return
        counter[t] -= 1
    print('YES')


N = int(input())
D = list(map(int, input().split()))
_ = input()
T = list(map(int, input().split()))
solve()
