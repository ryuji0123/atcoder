
if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    
    B = sorted(A)
    for n in A:
        if B[-1] != n:
            print(B[-1])
        else:
            print(B[-2])
