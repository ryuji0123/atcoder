def solve():
    for idx, c in enumerate(S):
        if c != '1' or idx == K - 1:
            print(c)
            return


S = input()
K = int(input())
solve()
