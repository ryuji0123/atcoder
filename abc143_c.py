class Stack(object):
    def __init__(self):
        self.container = []

    def __len__(self):
        return len(self.container)

    def push(self, elem):
        self.container.append(elem)

    def pop(self):
        index = len(self.container) - 1
        if index < 0:
            return None
        ret = self.container[index]
        del self.container[-1]
        return ret
    
    def compare(self, val):
        return self.container[-1] == val

if __name__ == '__main__':
    N = int(input())
    S = input()
    stack = Stack()
    stack.push(S[0])
    for s in S[1:]:
        if not stack.compare(s):
            stack.push(s)
    print(stack.__len__())
