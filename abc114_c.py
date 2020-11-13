# time: O(3^10)
# space: O(3^10)

def solve():
    def dfs():
        if 0 < len(nums) and N < int(''.join(nums)):
            return
        ret[0] += all([1 <= counter[k] for k in keys])

        for k in keys:
            nums.append(k)
            counter[k] += 1
            dfs()
            nums.pop()
            counter[k] -= 1


    keys = ['7', '5', '3']
    counter = {k: 0 for k in keys}
    nums = []
    ret = [0]
    dfs()
    print(ret[0])


N = input()
N = int(N)
solve()
