def solve(X, Y, p, q, r):
    red_apples = sorted(p, reverse=True)[: X]
    green_apples = sorted(q, reverse=True)[: Y]
    white_apples = sorted(r)

    ret = 0
    while red_apples and green_apples:
        if not white_apples or (white_apples[-1] < red_apples[-1] and white_apples[-1] < green_apples[-1]):
            return ret + sum(red_apples) + sum(green_apples)

        ret += white_apples.pop(-1)
        if red_apples[-1] < green_apples[-1]:
            red_apples.pop(-1)
        else:
            green_apples.pop(-1)


    if not red_apples:
        while green_apples and white_apples and (green_apples[-1] < white_apples[-1]):
            ret += white_apples.pop(-1)
            green_apples.pop(-1)
        return ret + sum(green_apples)

    else:
        while red_apples and white_apples and (red_apples[-1] < white_apples[-1]):
            ret += white_apples.pop(-1)
            red_apples.pop(-1)
        return ret + sum(red_apples)

if __name__ == '__main__':
    X, Y, A, B, C = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    print(solve(X, Y, p, q, r))