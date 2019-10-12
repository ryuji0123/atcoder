if __name__ == '__main__':
    N = int(input())
    H = [int(n) for n in input().split()]
    nums = H[::-1]
    ret = 'Yes'
    for idx, n in enumerate(nums[1:]):
        if n >= nums[idx] + 2:
            ret = 'No'
        elif n == nums[idx] + 1:
            nums[idx + 1] -= 1
    print(ret)
