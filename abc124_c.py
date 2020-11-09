def solve():
    N = len(S)
    from_zero_count = from_one_count = 0
    for idx in range(N):
        if idx % 2 == 0:
            from_zero_count += S[idx] == '1'
            from_one_count += S[idx] == '0'
        else:
            from_zero_count += S[idx] == '0'
            from_one_count += S[idx] == '1'
    print(min(from_zero_count, from_one_count))


S = input()
solve()
