from collections import deque

class Queue:
    def __init__(self, impl_type):
        if impl_type == "list":
            self.impl = []
        elif impl_type == "deque":
            self.impl = deque()
        else:
            raise ValueError("Invalid implementation type")

    def add(self, value):
        self.impl.append(value)

    def get(self):
        return self.impl[0]

    def remove(self):
        if type(self.impl) is list:
            return self.impl.pop(0)
        else:
            return self.impl.popleft()

    def size(self):
        return len(self.impl)

    def clear(self):
        self.impl.clear()

    def change_impl(self, impl_type):
        new_impl = []
        if impl_type == "list":
            new_impl = []
        elif impl_type == "deque":
            new_impl = deque()
        else:
            raise ValueError("Invalid implementation type")

        while self.size() > 0:
            new_impl.append(self.remove())

        self.impl = new_impl

# tests below
# queue = Queue("list")
# queue.add(1)
# queue.add("e")
# queue.add(3)
# print(queue.get())  
# queue.remove()
# print(queue.get())  
# print(queue.size()) 
# queue.change_impl("deque")
# print(queue.get())  
# queue.clear()
# print(queue.size()) 