def isPrime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

def solve():
    n = X
    while True:
        if isPrime(n):
            print(n)
            return
        n += 1

X = int(input())
solve()
