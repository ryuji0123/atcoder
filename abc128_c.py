import numpy as np

def countMatchedSwitch(sw_status, switch, index):
    ret = 0
    for s in switch[index]:
        if int(sw_status[int(s) - 1]) == 1:
            ret += 1
    return ret % 2


if __name__ == '__main__':
    N, M = [int(i) for i in input().split()]
    s = []
    for i in range(int(M)):
        data = input().split()
        s.append(data[1:])
    p = [int(i) for i in input().split()]
    
    ret = 0
    for i in range(2**N):
        is_all_passed = True
        sw_status = bin(i)[2:].zfill(N)
        for j in range(M):
            if p[j] != countMatchedSwitch(sw_status, s, j):
                is_all_passed = False
        if is_all_passed:
            ret += 1
    print("{ret}".format(ret=ret))
