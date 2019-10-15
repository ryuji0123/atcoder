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
    string = [int(i) for i in input()]
    ret = 0
    stack = Stack()
    stack.push(string[0])
    for s in string[1:]:
        if stack.__len__() == 0:
            stack.push(s)
            continue
        if stack.compare(s):
            stack.push(s)
        else:
            ret += 2
            stack.pop()

    print(ret)
