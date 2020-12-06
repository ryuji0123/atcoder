from itertools import product


def solve():
    N = len(S)
    ret = 0
    for bits in product(range(2), repeat=N - 1):
        equation = S[0]
        for idx, bit in enumerate(bits):
            equation += '+' if bit == 1 else ''
            equation += S[idx + 1]
        ret += eval(equation)
    print(ret)


S = input()
solve()
