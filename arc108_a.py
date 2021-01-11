def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def solve():
    divs = make_divisors(P)
    for d in divs:
        if (S - d) * d == P:
            print('Yes')
            return
    print('No')


S, P = map(int, input().split())
solve()
