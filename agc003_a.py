def solve():
    d = {k: 1 if k in S else -1 for k in 'EWSN'}
    print('Yes' if all([d['E'] * d['W'] == 1, d['N'] * d['S'] == 1]) else 'No')


S = input()
solve()
