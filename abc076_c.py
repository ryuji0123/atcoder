def solve():
    ls, lt = len(S), len(T)
    ret = []
    for i in range(ls - lt + 1):
        j = 0
        tmp = []

        is_valid = True
        while j < lt:
            if S[i + j] == '?' or S[i + j] == T[j]:
                tmp.append(T[j])
            else:
                is_valid = False
                break
            j += 1
        if is_valid:
            ret.append(S[: i].replace('?', 'a') + ''.join(tmp) + S[i + lt: ].replace('?', 'a'))
    
    print(sorted(ret)[0] if 0 < len(ret) else 'UNRESTORABLE')


S = input()
T = input()
solve()
