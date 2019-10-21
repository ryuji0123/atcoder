from math import sqrt
from fractions import gcd

def factorization(n):
    arr = []
    tmp = n
    for div in range(2, int(sqrt(n)) + 2):
        if tmp % div == 0:
            cnt = 0
            while tmp % div == 0:
                cnt += 1
                tmp //= div
            arr.append([div, cnt])

    if tmp != 1:
        arr.append([tmp, 1])

    if len(arr) == 0:
        arr.append([n, 1])

    return arr

if __name__ == '__main__':
    A, B = map(int, input().split())
    g = gcd(A, B)
    if g == 1:
        print(1)
        exit()
    facts = factorization(g)
    print(len(facts) + 1)

