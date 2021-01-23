from itertools import product


def solve():
    T = ['KIH', 'B', 'R', '']
    N = len(T)
    for pres in product(['A', ''], repeat=N):
        if S == ''.join([pres[i] + T[i] for i in range(N)]):
            print('YES')
            return
    print('NO')


S = input()
solve()
