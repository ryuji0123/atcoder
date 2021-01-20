def solve():
    idx = 0
    target = 'keyence'
    N = len(target)
    for s in S:
        idx += s == target[idx]
        if idx == N:
            print('YES')
            return
    print('NO')


S = input()
solve()
