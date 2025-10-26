class Node:
    def __init__(self, value): 
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        """
        create a new node
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self): 
        temp = self.head
        while temp is not None: 
            print(temp.value)
            temp = temp.next

    def append(self, value): 
        """
        create a new node
        add node to end
        """
        new_node = Node(value)

        # edge case: LinkedList 為空
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        # 其餘一般情況
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self): 
        # edge case: LinkedList 為空
        if self.length == 0: 
            return None
        # edge case: LinkedList 只有一個元素
        # elif self.length == 1: 
        #     self.head = None
        #     self.tail = None
        # 其餘一般情況
        pre = self.head
        temp = self.head
        while temp.next is not None: 
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0: 
            self.head = None
            self.tail = None

        return temp
    

    def get(self, index): 
        if index < 0 or index >= self.length: 
            return None
        temp = self.head
        for _ in range(index): 
            temp = temp.next

        return temp
    

    def set_value(self, index, value): 
        # if index < 0 or index >= self.length: 
        #     return None
        # temp = self.head
        # for _ in range(index): 
        #     temp = temp.next
        temp = self.get(index)
        if temp: 
            temp.value = value
            return True
        return False
    

    def prepend(self, value):
        """
        create a new node
        add node to beginning
        """
        new_node = Node(value)

        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        
        else: 
            new_node.next = self.head
            self.head = new_node
        self.length += 1
            
        return True
    

    def pop_first(self):
        if self.length == 0: 
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0: 
            self.tail = None
        return temp


    def insert(self, index, value): 
        """
        create a new node
        insert node to the place index
        """
        if index < 0 or index > self.length: 
            return False
        elif index == 0: 
            return self.prepend(value)
        elif index == self.length: 
            return self.append(value)     
        else: 
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1
        return True
    

    def remove(self, index): 
        if index < 0 or index >= self.length: 
            return None
        elif index == 0: 
            return self.pop_first()
        elif index == self.length - 1: 
            return self.pop()
        else: 
            """
            透過取prev.next取temp(O(1))
            相較直接用temp = self.get(index)(也可以O(n))
            此方式效率更高
            """
            prev = self.get(index - 1)
            # temp = self.get(index)
            temp = prev.next

            prev.next = temp.next
            temp.next = None
            self.length -= 1
        return temp
    
    # Important! **Interview Question**
    def reverse(self): 
        # self.head, self.tail = self.tail, self.head
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length): 
            after = temp.next
            temp.next = before
            before = temp
            temp = after



my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

my_linked_list.print_list()
print("----------------------")

my_linked_list.reverse()

my_linked_list.print_list()