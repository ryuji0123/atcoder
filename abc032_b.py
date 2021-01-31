def solve():
    ret = set()
    ls = len(s)
    for i in range(ls - k + 1):
        ret.add(s[i: i + k])
    print(len(ret))


s = input()
k = int(input())
solve()
