def solve():
    ret = []
    for c in s:
        if c == 'B':
            if 0 < len(ret):
                ret.pop()
        else:
            ret.append(c)
    print(''.join(ret))


s = input()
solve()
