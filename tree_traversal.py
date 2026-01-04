"""
Tree_traversal(遍歷樹) := Visit every nodes in the tree and put into a list
then return the list

遍歷樹通常有兩種方法 : 
1. Breadth First Search(BFS) : 廣度優先搜尋，從根開始逐層遍歷(由上至下、由左至右)

2. Depth First Search(DFS) : 深度優先搜尋，從leave開始遍歷(由下往上、由左至右)
"""

class Node:
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None

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
    
    # 上面都跟tree.py相同
    # 定義兩種遍歷方式
    # --------------------------------------------------------------------
    
    # BFS: 廣度優先 -- 由上至下遍歷
    def BFS(self): 
        # 從root開始
        current_node = self.root
        queue = []
        results = []

        # while loop 前必須先將root放進queue
        queue.append(current_node)

        # 由於我們會將同一層的node依序放進queue中，因此必然是從上到下遍歷
        while len(queue) > 0: 
            # 將queue中的第一個元素移除並賦值給current_node
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None: 
                queue.append(current_node.left)
            if current_node.right is not None: 
                queue.append(current_node.right)
        
        return results
    
    # DFS preorder: 深度優先(前序) -- 由上至下，由左至右
    def dfs_pre_order(self): 
        results = []

        def traverse(current_node): 
            results.append(current_node.value)
            if current_node.left is not None: 
                traverse(current_node.left)
            if current_node.right is not None: 
                traverse(current_node.right)
                
        traverse(self.root)
        return results
    
    # DFS postorder: 深度優先(後序)
    # 依序訪問 left -> right -> parent(root)
    def dfs_post_order(self): 
        results = []

        def traverse(current_node): 
            if current_node.left is not None: 
                traverse(current_node.left)
            if current_node.right is not None: 
                traverse(current_node.right)
            results.append(current_node.value)
                
        traverse(self.root)
        return results
    
    # DFS inorder: 深度優先(中序)
    # 依序訪問 left -> parent(root) -> right
    def dfs_in_order(self): 
        results = []

        def traverse(current_node): 
            if current_node.left is not None: 
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None: 
                traverse(current_node.right)
                
        traverse(self.root)
        return results





my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())
print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())