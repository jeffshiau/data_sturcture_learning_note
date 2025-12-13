class Node:
    def __init__(self, value): 
        self.value = value
        self.next = None

# LIFO(Last In First Out)
# 返回上一步的功能就是利用stack實現
class Stack: 
    def __init__(self, value): 
        new_node = Node(value)
        self.top = new_node
        # self.buttom = new_node
        self.height = 1

    def print_stack(self): 
        temp = self.top
        while temp is not None: 
            print(temp.value)
            temp = temp.next

    def push(self, value): 
        new_node = Node(value)
        if self.height == 0: 
            self.top = new_node
        else: 
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self): 
        if self.height == 0: 
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


# my_stack = Stack(3)
# my_stack.push(2)
# my_stack.push(1)
# my_stack.pop()

# my_stack.print_stack()




# FIFO(First In First Out)
class Queue: 
    def __init__(self, value): 
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self): 
        temp = self.first
        while temp is not None: 
            print(temp.value)
            temp = temp.next

    # 新增
    def enqueue(self, value): 
        new_node = Node(value)
        if self.first is None: 
            self.first = None
            self.last = None
        else: 
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    # 移除
    def dequeue(self): 
        if self.length == 0: 
            return None
        temp = self.first
        if self.length == 1: 
            self.first = None
            self.last = None
        else: 
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp



my_queue = Queue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)

my_queue.dequeue()

my_queue.print_queue()
