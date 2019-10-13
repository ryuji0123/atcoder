if __name__ == '__main__':
    N = int(input())
    string = {}
    ret = 0
    for n in range(N):
        cur_char = ''.join(sorted(input()))
        if cur_char in string:
            ret += string[cur_char]
        string[cur_char] = string.get(cur_char, 0) + 1
    print(ret)
