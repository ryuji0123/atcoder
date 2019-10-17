def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)

if __name__ == '__main__':
    N = int(input())
    nums = [int(n) for n in input().split()]
    if len(nums) == 1:
        print(nums[0])
        exit()
    
    ret = gcd(nums[0], nums[1])
    for n in nums[1:]:
        ret = gcd(ret, n)    
    print(ret)
