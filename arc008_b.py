from collections import Counter


def solve():
    name_counter = Counter(name)
    kit_counter = Counter(kit)
    ret = 0
    for e, c in name_counter.items():
        if e not in kit_counter:
            print(-1)
            return
        ret = max(ret, c // kit_counter[e] + int(c % kit_counter[e] != 0))
    print(ret)


_ = input()
name = input()
kit = input()
solve()
