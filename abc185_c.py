def solve():
    print(cmb(L - 1, 11))

def cmb(n, r):
    return fact[n] // fact[n - r] // fact[r]

L = int(input())
fact = [1]
for i in range(1, L + 1):
    fact.append(fact[i - 1] * i)
solve()
