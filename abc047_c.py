def solve():
    ret = 0
    cur = S[0]
    for i in range(1, len(S)):
        if cur != S[i]:
            cur = S[i]
            ret += 1
    print(ret)


S = input()
solve()
