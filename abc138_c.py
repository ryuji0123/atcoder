
if __name__ == '__main__':
    N = int(input())
    values = sorted([int(n) for n in input().split()], reverse=True)
    ret = 0
    while len(values) > 1:
        tmp = (values[-1] + values[-2]) / 2
        del values[-1]
        values[-1] = tmp
    print(values[0])
