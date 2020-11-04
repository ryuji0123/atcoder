def solve():
    print(sum([B[0]] + [min(bi, bj) for bi, bj in zip(B, B[1: ])] + [B[-1]]))


N = input()
B = list(map(int, input().split()))
solve()
