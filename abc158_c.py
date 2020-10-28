def solve():
    for i in range(1, 10001):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            return
    print(-1)

A, B = map(int, input().split())
solve()
