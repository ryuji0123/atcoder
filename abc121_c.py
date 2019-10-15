
if __name__ == '__main__':
    N, M = [int(n) for n in input().split()]
    A = []
    for n in range(N):
        A.append([int(n) for n in input().split()])
    
    vals = sorted(A, key=lambda x: x[0])
    ret = 0
    for v in vals:
        if v[1] < M:
            M -= v[1]
            ret += v[0] * v[1]
        else:
            print(ret + v[0] * M)
            exit()
