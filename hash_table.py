"""
Ways to Dealing Collision
Separate Chaining Hashing : 允許一個address儲存多個(key, value)
Linear Probing(open addressing) : 一個address僅能儲存一個(key, value)，若遇到該address已有資料，則順延至下一個address儲存
"""

"""
要確認hash table的Big O，必須先確認該hash table中hash function的Big O
若忽略hash function的複雜度(假設其為O(1))，則
set_item為O(1)
get_item為O(n)(最糟情況，所有資料存在同一address)，一般情況為O(n)(資料均勻分布)
"""

# size最好用質數，以盡可能避免collision
class HashTable: 
    def __init__(self, size = 7): 
        self.data_map = [None] * size
    
    def __hash(self, key): 
        my_hash = 0
        for letter in key: 
            # 自訂hash function
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash
    
    def print_table(self): 
        for i, val in enumerate(self.data_map): 
            print(i, ":", val)
    
    def set_item(self, key, value): 
        index = self.__hash(key)
        if self.data_map[index] is None: 
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key): 
        index = self.__hash(key)
        if self.data_map[index] is not None: 
            for i in range(len(self.data_map[index])): 
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    # get all keys in this hash_table
    def keys(self): 
        all_keys = []
        for idx in range(len(self.data_map)): 
            if self.data_map[idx] is not None: 
                for i in range(len(self.data_map[idx])): 
                    all_keys.append(self.data_map[idx][i][0])
        return all_keys





my_hash_table = HashTable()
my_hash_table.print_table()

print("--------------------------------")

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)
my_hash_table.set_item("lumber", 70)
my_hash_table.print_table()

print("--------------------------------")

# print(my_hash_table.get_item("bolts"))
# print(my_hash_table.get_item("Jeff"))
print(my_hash_table.keys())