"""
Docstring for recursive_binary_search_tree
可參考tree.py : 內容相同，只是將calss中的部分method改用reclusion寫
"""
class Node:
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
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

    # 從這邊開始不同，改用遞迴完成
    def __r_contains(self, current_node, value): 
        if current_node == None: 
            return False
        if value == current_node.value: 
            return True
        if value < current_node.value: 
            return self.__r_contains(current_node.left, value)
        elif value > current_node.value: 
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value): 
        return self.__r_contains(self.root, value)
    

    def __r_insert(self, current_node, value): 
        if current_node == None: 
            return Node(value)
        if value < current_node.value: 
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value: 
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value): 
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)


    # sub method of delete_node
    def min_value(self, current_node): 
        while current_node.left is not None: 
            current_node = current_node.left
        return current_node.value

    # 刪除節點
    def __delete_node(self, current_node, value): 
        """
        Docstring for __delete_node
        
        比較複雜，需要根據刪除目標節點的位置進行不同操作
        1. leave node : 最簡單，直接刪除
        2. 該node下僅有一邊有分支 : 直接將該node刪除，並將下方分支拉上來取代
        3. 該node下兩邊都有分支 : 將右分支的左邊node複製給目標node再將下方node移除
        """
        if current_node == None: 
            return None
        if value < current_node.value: 
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value: 
            current_node.right = self.__delete_node(current_node.right, value)
        # 找到目標node
        else: 
            # 1. removing leave node
            if current_node.left == None and current_node.right == None: 
                return None
            # 2. removing node only has right item
            elif current_node.left == None: 
                current_node = current_node.right
            # 3. removing node only has left item
            elif current_node.right == None: 
                current_node = current_node.left
            # 4. removing node has both left and right item (complex)
            else: 
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node
    
    def delete_node(self, value): 
        self.root = self.__delete_node(self.root, value)
    




my_tree = BinarySearchTree()
# my_tree.insert(47)
# my_tree.insert(21)
# my_tree.insert(76)
# my_tree.insert(18)
# my_tree.insert(27)
# my_tree.insert(52)
# my_tree.insert(82)

# print("BST Contains 27:")
# print(my_tree.r_contains(27))

# print("BST Contains 17:")
# print(my_tree.r_contains(17))

# ------------------------------------------------

# print(my_tree.min_value(my_tree.root))
# print(my_tree.min_value(my_tree.root.right))

# ------------------------------------------------
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

print("Root", my_tree.root.value)
print("Root -> left", my_tree.root.left.value)
print("Root -> right", my_tree.root.right.value)

my_tree.delete_node(2)
print("Root", my_tree.root.value)
print("Root -> left", my_tree.root.left.value)
print("Root -> right", my_tree.root.right)