# time: O(NlogN)
# space: O(N)
from collections import Counter


def solve():
    even_counter, odd_counter = Counter(), Counter()
    for idx, v in enumerate(V):
        if idx % 2 == 0:
            even_counter[v] += 1
        else:
            odd_counter[v] += 1

    even_most_commons = even_counter.most_common()[:2]
    odd_most_commons = odd_counter.most_common()[:2]
    even_e, even_c = even_most_commons[0]
    odd_e, odd_c = odd_most_commons[0]
    if odd_e != even_e:
        print(N - odd_c - even_c)
    else:
        even_c2 = even_most_commons[1][1] if len(even_most_commons) == 2 else 0
        odd_c2 = odd_most_commons[1][1] if len(odd_most_commons) == 2 else 0
        print(min(N - odd_c - even_c2, N - odd_c2 - even_c))


N = int(input())
V = list(map(int, input().split()))
solve()
