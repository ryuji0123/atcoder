def solve():
    print(sum([
        groups[keys[i]] * groups[keys[j]] * groups[keys[k]]
        for i in range(5)
        for j in range(i + 1, 5)
        for k in range(j + 1, 5)
        ]))


keys = 'MARCH'
groups = {k: 0 for k in keys}
N = int(input())
for _ in range(N):
    s = input()
    if s[0] in groups:
        groups[s[0]] += 1
solve()
