class Node: 
    def __init__(self, value): 
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList: 
    def __init__(self, value): 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    

    def print_list(self): 
        temp = self.head
        while temp: 
            print(temp.value)
            temp = temp.next


    def append(self, value): 
        new_node = Node(value)

        if self.length == 0: 
        # if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0: 
            return None
        temp = self.tail
        if self.length == 1: 
            self.head = None
            self.tail = None
        else: 
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1

        return temp
    
    def prepend(self, value): 
        new_node = Node(value)
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0: 
            return None
        temp = self.head
        if self.length == 1: 
            self.head = None
            self.tail = None     
        else: 
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1    
        return temp
    

    def get(self, index): 
        if index < 0 or index >= self.length: 
            return None
        temp = self.head
        # linked list寫法，也適用於doubly linked list，但可以優化
        # for _ in range(index): 
        #     temp = temp.next
        if index < self.length / 2: 
            for _ in range(index): 
                temp = temp.next
        else: 
            temp = self.tail
            for _ in range(self.length - 1 ,index, -1): 
                temp = temp.prev
        return temp

    def set_value(self, index, value): 
        temp = self.get(index)
        if temp: 
            temp.value = value
            return True
        return False
    
    def insert(self, index, value): 
        if index < 0 or index > self.length: 
            return None
        elif index == 0: 
            return self.prepend(value)
        elif index == self.length: 
            return self.append(value)
        else: 
            new_node = Node(value)
            before = self.get(index - 1)
            after =  before.next

            before.next = new_node
            new_node.next = after
            after.prev = new_node
            new_node.prev = before
        self.length += 1
        return True
    
    def remove(self, index): 
        if index < 0 or index >= self.length: 
            return None
        elif index == 0: 
            return self.pop_first()
        elif index == self.length: 
            return self.pop()
        else: 
            temp = self.get(index)
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None
        self.length -= 1
        return 0



my_doubly_linked_list = DoublyLinkedList(1)

my_doubly_linked_list.append(5)

my_doubly_linked_list.insert(1, 3)


my_doubly_linked_list.print_list()