def solve():
    depth = 1
    tmp = 1
    while 2 * tmp <= N:
        tmp *= 2
        depth += 1
    cur = 1
    d = 1
    while True:
        if d % 2 == 1:
            cur = cur * 2 + 1 if depth % 2 == 1 else cur * 2
        else:
            cur = cur * 2 + 1 if depth % 2 == 0 else cur * 2
        if N < cur:
            print('Takahashi' if d % 2 == 0 else 'Aoki')
            return
        d += 1


N = int(input())
solve()
