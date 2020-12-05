from collections import Counter


MOD = pow(10, 9) + 7


def solve():
    counter = Counter(A)
    if N % 2 == 0:
        is_valid = True
        for i in range(1, N, 2):
            is_valid = is_valid and counter[i] == 2
    else:
        is_valid = counter[0] == 1
        for i in range(2, N, 2):
            is_valid = is_valid and counter[i] == 2

    print(pow(2, N // 2) % MOD if is_valid else 0)


N = int(input())
A = list(map(int, input().split()))
solve()
