N = int(input())
A = map(int, input().split())

accumulated_sums = []
tmp = 0
for a in A:
    tmp += a
    accumulated_sums.append(tmp)

min_cost = 2020202020
for ac_s in accumulated_sums:
    cur_cost = abs(accumulated_sums[-1] - 2 * ac_s)
    min_cost = min(min_cost, cur_cost)

print(min_cost)
