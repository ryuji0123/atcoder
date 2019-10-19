if __name__ == '__main__':
    N = int(input())
    d = [int(i) for i in input().split()]
    ret = 0
    for i, v in enumerate(d):
        for j in d[i + 1:]:
            ret += v * j
    print(ret)
