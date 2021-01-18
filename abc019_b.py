def solve():
    N = len(s)
    idx = 0
    count = 0
    cur = None
    ret = [[None, 0]]
    while idx < N:
        cur = s[idx]
        if cur != ret[-1][0]:
            ret.append([cur, 1])
        else:
            ret[-1][1] += 1
        idx += 1
    print(''.join([c + str(num) for c, num in ret[1: ]]))


s = input()
solve()
