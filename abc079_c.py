from itertools import product

REPEAT = 3


def solve():
    for operators in product(['-', '+'], repeat=REPEAT):
        eq = ''.join([operands[idx] + operators[idx] for idx in range(REPEAT)] + [operands[-1]])
        if eval(eq) == 7:
            print(eq + '=7')
            return


operands = input()
solve()
