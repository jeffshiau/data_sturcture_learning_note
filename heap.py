"""
heap(堆積)) 是 complete tree(由左至右)
可以是top node最大，也能是leave最大(但須統一)
左右大小不比較
heap 不擅長被搜索

我們會將heap依序存在一個list中(僅存數字)而非字典，也不會額外建立node
儲存方式可以直接從index = 0開始，也可以從index = 1開始(推薦，數學計算較簡單)

** 若從index = 1開始存 : 
left_child index = 2 * parent_index
right_child index = 2 * parent_index + 1

parent_index = child_index // 2
"""

"""
priority queue : 可以用heap實現(較高效率)
也能用linked list實現(較低效率)
"""

class MaxHeap: 
    def __init__(self): 
        self.heap = []

    def _left_child(self, index): 
        # if start from index 0
        return 2 * index + 1

        # if start from index 0
        # return 2 * index
    
    def _right_child(self, index): 
        # if start from index 0
        return 2 * index + 2

        # if start from index 0
        # return 2 * index + 1
    
    def _parent(self, index): 
        # if start from index 0
        return (index - 1) // 2

        # if start from index 0
        # return index // 2
    
    def _swap(self, index1, index2): 
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index = 0): 
        """
        比較目標元素(index)與其左右child的值
        若index元素比child小，則將其跟'較大的'child換位置 
        """
        max_index = index
        while True: 
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            # 也可以，但要加判斷沒有child的例外
            # sub_max_index = max(left_index, right_index)
            # if self.heap[sub_max_index] > self.heap[index]: 
            #     max_index = sub_max_index
            #     self._swap(index, sub_max_index)
            #     index = sub_max_index
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]: 
                max_index = left_index

            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]: 
                max_index = right_index

            if max_index != index: 
                self._swap(index, max_index)
                index = max_index
            else: 
                return


    def insert(self, value): 
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]: 
            self._swap(current, self._parent(current))
            current = self._parent(current)
    
    def remove(self): 
        """
        在heap中永遠只會remove top node
        remove後最麻煩的問題是要如何重新排列，並使其仍為complete tree
        """
        if len(self.heap) == 0: 
            return None
        
        # 同時移除heap中唯一元素並回傳該元素
        if len(self.heap) == 1: 
            return self.heap.pop()
        
        # 移除的元素
        max_value = self.heap[0]

        # 將最後的元素移除並暫放到最前面(top)
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value


def find_kth_smallest(nums, k):
    # Initialize a new instance of MaxHeap
    max_heap = MaxHeap()
 
    # Loop over each number in the input list
    for num in nums:
        # Insert the current number into the heap.
        # The heap maintains its properties automatically
        max_heap.insert(num)
        
        # If the heap size exceeds k, remove the maximum element.
        # This keeps the heap size at k and ensures it only contains
        # the smallest k numbers seen so far
        if len(max_heap.heap) > k:
            max_heap.remove()
 
    # After the loop, the heap contains the smallest k numbers.
    # The root of the heap is the kth smallest number,
    # remove and return it as the function's result.
    return max_heap.remove()



myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print("initial")
print(myheap.heap)

myheap.remove()

print("remove 1")
print(myheap.heap)

myheap.remove()

print("remove 2")
print(myheap.heap)