# time: O(N^(1/2))
# space: O(1)

def solve():
    i = 1
    ret = float('inf')
    while i * i <= N:
        if N % i == 0:
            ret = min(ret, i - 1 + N // i - 1)
        i += 1
    print(ret)


N = int(input())
solve()
