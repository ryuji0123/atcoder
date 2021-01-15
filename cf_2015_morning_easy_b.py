def solve():
    if N % 2 != 0:
        print(-1)
        return

    bias = N // 2
    print(sum([s[i] != s[i + bias] for i in range(bias)]))


N = int(input())
s = input()
solve()
