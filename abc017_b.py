def solve():
    idx = 0
    N = len(X)
    while idx < N:
        if X[idx] in 'oku':
            idx += 1
            continue
        if X[idx: idx + 2] == 'ch':
            idx += 2
            continue
        print('NO')
        return
    print('YES')


X = input()
solve()
