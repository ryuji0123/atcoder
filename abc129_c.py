BASE =  1000000007

if __name__ == '__main__':
    N, M = [int(i) for i in input().split()]
    not_available = []
    for i in range(M):
        not_available.append(int(input()))
    x = 0
    y = 1
    predicted_next = 1 
    is_available = [True] * N
    for idx in not_available:
        is_available[idx - 1] = False
    
    for flag in is_available:
        if flag:
            z = x + y
            x = y
            y = z
        else:
            x = y
            y = 0

    print(y % BASE)
