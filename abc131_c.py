def getDivisableCount(min_bound, max_bound, div):
    return max_bound // div - (min_bound - 1) // div

def LCM(a, b):
    return a * b // GCD(a, b)

def GCD(a, b):
    if a > b:
        a, b = b, a
    while b % a != 0:
        a, b = b % a, a
    return a

if __name__ == '__main__':
    A, B, C, D = [int(i) for i in input().split()]
    ret = (B - A + 1) - getDivisableCount(A, B, C) - getDivisableCount(A, B, D) + getDivisableCount(A, B, LCM(C, D))
    print(ret)
