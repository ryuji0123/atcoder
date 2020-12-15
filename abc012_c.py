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
    n = 2025 - N
    arr = make_divisors(n)
    for a in arr:
        if 10 <= a or 10 <= n // a:
            continue
        print(f'{a} x {n // a}')


N = int(input())
solve()
