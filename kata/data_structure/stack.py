class BasicStack():
    def __init__(self):
        self.pool = []

    def pop(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        return self.pool == []

    def size(self):
        return len(self.pool)


class LeftStack(BasicStack):
    """
    左端栈顶
    """
    def push(self, item):
        return self.pool.insert(0, item)

    def peek(self):
        return self.pool[0]


class RightStack(BasicStack):
    """
    右端栈顶
    """
    def push(self, item):
        return self.pool.append(item)

    def pop(self):
        return self.pool.pop()

    def peek(self):
        return self.pool[-1]


if __name__ == "__main__":
    l_stack = LeftStack()
    l_actions = [
        l_stack.is_empty(),
        l_stack.push(1),
        l_stack.push("aa"),
        l_stack.peek(),
        l_stack.push(False),
        l_stack.pop()
    ]
    print(l_stack.pool)
    print(l_actions)

    r_stack = RightStack()
    r_actions = [
        r_stack.is_empty(),
        r_stack.push("a"),
        r_stack.push(4),
        r_stack.peek(),
        r_stack.push(True),
        r_stack.is_empty(),
        r_stack.push(8.4),
        r_stack.pop()
    ]
    print(r_stack.pool)
    print(r_actions)
