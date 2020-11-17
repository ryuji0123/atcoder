from itertools import permutations


def solve():
    ret = 0
    for nums in permutations(range(1, N)):
        nums = sorted([(idx + 1, n) for idx, n in enumerate(nums)], key=lambda x: x[1])
        ret += sum([T[i][j] for (i, _), (j, _) in zip(nums, nums[1: ])]) == (K - T[0][nums[0][0]] - T[nums[-1][0]][0])
    print(ret)


N, K = map(int, input().split())
T = []
for _ in range(N):
    T.append(list(map(int, input().split())))
solve()
