X, Y = map(int, input().split())
ret = 0
if X == 1:
    ret += 300000
elif X == 2:
    ret += 200000
elif X == 3:
    ret += 100000

if Y == 1:
    ret += 300000
elif Y == 2:
    ret += 200000
elif Y == 3:
    ret += 100000
if X == 1 and Y == 1:
    ret += 400000
print(ret)
