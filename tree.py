class Node:
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None

"""
    Full Tree: 每個節點都有0或2個子節點
    Perfect Tree: 每個節點都有2個子節點(除了leaf(最末端的節點))，有2^n-1個節點
    Conplete Tree: 資料從左至右填入節點


    binary search tree(BST): 大的在右，小的在左
    考慮最糟情況，若此BST沒有任何fork(分支)，則此時即為一個linked list，CRUD複雜度皆為O(n)
    若此BST是perfect tree，則為最佳情況O(log n)(更嚴謹應該說Omega(log n))
    一般而言還是會說BST複雜度為O(log n)
"""

class BinarySearchTree:
    # # 一般寫法，初始化BST時直接給root值
    # def __init__(self, value): 
    #     new_node = Node(value)
    #     self.root = new_node

    # 也可以先見一個空的BST，後續再給值
    def __init__(self,): 
        self.root = None

    def insert(self, value): 
        new_node = Node(value)
        if self.root == None: 
            self.root = new_node
            return True
        
        temp = self.root
        while True: 
            if new_node.value == temp.value: 
                return False
            elif new_node.value < temp.value: 
                if temp.left is None: 
                    temp.left = new_node
                    return True
                else: 
                    temp = temp.left
            else: 
                if temp.right is None: 
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value): 
        # if self.root is None: 
        #     return False
        temp = self.root
        while temp: 
            if value < temp.value: 
                temp = temp.left
            elif value > temp.value: 
                temp = temp.right
            else: 
                return True
        return False



# my_tree = BinarySearchTree()
# my_tree.insert(2)
# my_tree.insert(1)
# my_tree.insert(3)

# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)

# print(my_tree.contains(5))
# print(my_tree.contains(3))


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(1)
bst.insert(8)
bst.insert(12)
bst.insert(20)

result1 = bst.contains(1)
result2 = bst.contains(8)
result3 = bst.contains(12)
result4 = bst.contains(20)
print(result1, result2, result3, result4)
