N = int(input())
a = list(map(int, input().split()))
broken = 0

for n in range(N):
    if a[n] != broken + 1:
        continue
    broken += 1

if broken == 0:
    print(-1)
else:
    print(N - broken)