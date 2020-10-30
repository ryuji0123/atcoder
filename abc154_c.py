def solve():
    ref = {}
    for i in A:
        if i in ref:
            print('NO')
            return
        ref[i] = 1
    print('YES')


N = int(input())
A = list(map(int, input().split()))
solve()
