def calcRestNum(a, b, ret):
    if a < b:
        ret += a
        b -= a
        a = 0
    else:
        ret += b
        a -= b
        b = 0
    return [a, b, ret]

if __name__ == '__main__':
    N = int(input())
    A = [int(a) for a in input().split()]
    B = [int(b) for b in input().split()]

    ret = 0
    for n in reversed(range(N)):
        A[n + 1], B[n], ret = calcRestNum(A[n + 1], B[n], ret)
        A[n], B[n], ret = calcRestNum(A[n], B[n], ret)
    print(ret)
