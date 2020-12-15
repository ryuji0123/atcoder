def factorization(n):
    arr = []
    tmp = n
    div = 2
    while div * div <= n:
        if tmp % div == 0:
            cnt = 0
            while tmp % div == 0:
                cnt += 1
                tmp //= div
            arr.append([div, cnt])
        div += 1

    if tmp != 1:
        arr.append([tmp, 1])

    if len(arr) == 0:
        arr.append([n, 1])

    return arr

def solve():
    ret = set()
    for a in A:
        tmp = 1
        divs = factorization(a)
        for e, c in divs:
            if e == 2:
                continue
            tmp *= pow(e, c)
        ret.add(tmp)
    print(len(ret))


N = input()
A = list(map(int, input().split()))
solve()
