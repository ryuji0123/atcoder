MOD = 12

def solve():
    cycle = ['W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    key = ['Do', '', 'Re', '', 'Mi', 'Fa', '', 'So', '', 'La', '', 'Si']
    for start in range(MOD):
        is_valid = True
        for j in range(20):
            if cycle[(start + j) % MOD] != S[j]:
                is_valid = False
                break
        if is_valid:
            print(key[start])
            return


S = input()
solve()
