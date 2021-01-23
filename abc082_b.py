def solve():
    ls, lt = len(s), len(t)
    sp = sorted(s)
    tp = sorted(t, reverse=True)
    idx = 0
    while idx < ls and idx < lt:
        if sp[idx] < tp[idx]:
            print('Yes')
            return
        if tp[idx] < sp[idx]:
            print('No')
            return
        idx += 1
    print('Yes' if ls < lt else 'No')


s = input()
t = input()
solve()
