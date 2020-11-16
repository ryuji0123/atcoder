from itertools import product


def solve():
    ret = float('inf')
    for vals in product(range(2), repeat=D):
        cost = score = 0
        rest = []
        for idx, bit in enumerate(vals):
            if bit == 1:
                cost += p[idx]
                score += 100 * (idx + 1) * p[idx] + c[idx]
            else:
                rest.append([100 * (idx + 1), p[idx] - 1])
        if score < G:
            diff = G - score
            additional_cost = float('inf')
            for point, limit in rest:
                if point * limit < diff:
                    continue
                additional_cost = min(additional_cost, diff // point + (0 < diff % point))
            cost += additional_cost
        ret = min(ret, cost)
    print(ret)


D, G = map(int, input().split())
p, c = [], []
for _ in range(D):
    tmp = list(map(int, input().split()))
    p.append(tmp[0])
    c.append(tmp[1])
solve()
