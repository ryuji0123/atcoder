def solve():
    s = S.split()
    ret = set()
    for c in s:
        if '@' not in c or c == '@':
            continue
        idx = 0
        N = len(c)
        while idx < N:
            if c[idx] == '@' and idx + 1 < N and c[idx + 1] != '@':
                idx += 1
                l = idx
                while idx < N and c[idx] != '@':
                    idx += 1
                ret.add(c[l: idx])
                continue
            idx += 1
    for r in sorted(ret):
        print(r)


S = input()
solve()
