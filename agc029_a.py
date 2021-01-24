def solve():
    count = ret = 0
    for c in S:
        if c == 'W':
            ret += count
        else:
            count += 1
    print(ret)


S = input()
solve()
