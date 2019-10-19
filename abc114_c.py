def appendedList(arr, val):
    ret = arr.copy()
    ret.append(val)
    return ret

def dfs(cur, target, ret):
    if 0 < len(cur):
        if target < int(''.join(map(str, cur))):
            return 0
    const = 1 if (3 in cur and 5 in cur and 7 in cur) else 0
    ret3 = dfs(appendedList(cur, 3), target, ret)
    ret5 = dfs(appendedList(cur, 5), target, ret)
    ret7 = dfs(appendedList(cur, 7), target, ret)
    return ret + const + ret3 + ret5 + ret7

if __name__ == '__main__':
    N = int(input())
    print(dfs([], N, 0))
