def solve():
    k = len(N)
    val = int(N)
    ret = float('inf')
    for i in range(pow(2, k)):
        tmp = count = 0
        for j in range(k):
            if i >> j & 1:
                tmp += int(N[j])
            else:
                count += 1
        if  count < k and tmp % 3 == 0:
            ret = min(ret, count)
    print(ret if ret != float('inf') else -1)


N = input()
solve()
