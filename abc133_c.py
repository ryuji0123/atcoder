def solve():
    MOD = 2019
    mod_list = [i % MOD for i in range(L, min(L + MOD + 1, R + 1))]
    print(min([mi * mj % MOD for i, mi in enumerate(mod_list) for mj in mod_list[i + 1: ]]))


L, R = map(int, input().split())
solve()
