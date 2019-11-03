N = int(input())
ret = 1 - 1 + N - 1
for div in range(2, int(N ** 0.5) + 1):
    if N % div != 0: continue
    ret = min(ret, div - 1 + N // div - 1)
print(ret)
