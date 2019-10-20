#def lowerBound(nums, target):
#    if nums[-1] < target: 
#        return -1
#    lp = 0
#    rp = len(nums) - 1
#    mp = lp + rp >> 1
#    while lp <= rp:
#        mp = lp + rp >> 1
#        if nums[mp] == target:
#            #print("Solved\nmp: ", mp)
#            return mp
#        if nums[mp] < target:
#            lp = mp + 1
#        else:
#            rp = mp - 1
#    #print("Not found\nmp: ", mp)
#    return mp if target < nums[mp] else -1

from bisect import *
if __name__ == '__main__':
    N = int(input())
    L = sorted(map(int, input().split()))
    print(sum(jdx - bisect(L, a - L[jdx], 0, jdx) for idx, a in enumerate(L) for jdx in range(idx)))
