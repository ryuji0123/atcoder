def solve():
    score = sum([E[i] in L for i in range(6)])
    if score == 6:
        ret = 1
    elif score == 5 and B in L:
        ret = 2
    elif score == 5:
        ret = 3
    elif score == 4:
        ret = 4
    elif score == 3:
        ret = 5
    else:
        ret = 0
    print(ret)


E = list(input().split())
B = input()
L = list(input().split())
solve()
