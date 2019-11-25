A, B, X = map(int, input().split())
ret = 0
N = pow(10, 9)
n = list(str(N))
if A * N + B * len(n) <= X:
    print(N)
    exit()
while X < A * N + B * len(n) and int(''.join(n)) != 0:
    N //= 10
    n = list(str(N))
for idx in range(len(n)):
    idx = int(idx)
    while True: 
        n[idx] = str(int(n[idx]) + 1)
        tmp = A * int(''.join(n)) + B * len(n)
        if X < tmp or n[idx] == '10':
            n[idx] = str(int(n[idx]) - 1)
            break
print(''.join(n))
