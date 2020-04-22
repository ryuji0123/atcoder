from collections import deque

def solve(K):
    stack = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for _ in range(K):
        num = stack.popleft()
        one_digit = num % 10
        if one_digit % 10 == 0:
            nexts = [num * 10, num * 10 + 1]
        elif one_digit % 10 == 9:
            nexts = [num * 10 + 8, num * 10 + 9]
        else:
            nexts = [num * 10 + one_digit - 1, num * 10 + one_digit, num * 10 + one_digit + 1]

        for n in nexts:
            stack.append(n)
    return num

if __name__ == '__main__':
    K = int(input())
    print(solve(K))
