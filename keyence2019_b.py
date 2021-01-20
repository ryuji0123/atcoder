def solve():
    T = 'keyence'
    ls = len(S)
    for i in range(ls):
        for j in range(i, ls + 1):
            if S[:i ] + S[j: ] == T:
                print('YES')
                return
    print('NO')

S = input()
solve()
