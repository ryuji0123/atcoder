def calc(a, b):
    return max(len(str(a)), len(str(b)))


def solve():
    ret = float('inf')
    i = 1
    while i ** 2 <= N:
        if N % i == 0:
            ret = min(ret, calc(i, N // i))
        i += 1
    print(ret)


N = int(input())
solve()
