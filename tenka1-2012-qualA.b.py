def solve():
    ret = []
    for idx, c in enumerate(s):
        if c != ' ':
            ret.append(c)
        else:
            if s[idx - 1] == ' ':
                continue
            ret.append(',')
    print(''.join(ret))
  

s = input()
solve()
