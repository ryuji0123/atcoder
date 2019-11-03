N = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        if not i * j == N: continue
        print('Yes')
        exit()
print('No')
