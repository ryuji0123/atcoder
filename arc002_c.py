from itertools import product


def solve():
    commands = 'ABXY'
    ret = float('inf')
    for l in product(commands, repeat=2):
        for r in product(commands, repeat=2):
            LR = [''.join(l), ''.join(r)]
            idx = count = 0
            while idx < N:
                if idx == N - 1:
                    count += 1
                    break
                
                if C[idx: idx + 2] in LR:
                    idx += 2
                else:
                    idx += 1
                count += 1
            ret = min(ret, count)
    print(ret)


N = int(input())
C = input()
solve()
