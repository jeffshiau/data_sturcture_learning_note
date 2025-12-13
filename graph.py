"""
常用 adjacency matrix 或 adjacency list 表示 graph
adjacency list 通常是比較有效率的選擇(除了刪除節點)
"""

class Graph: 
    def __init__(self): 
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list: 
            print(vertex, ":", self.adj_list[vertex])
    
    def add_vertex(self, vertex): 
        if vertex not in self.adj_list.keys(): 
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2): 
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): 
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2): 
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): 
            try: 
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError: 
                pass
            return True
        return False
    
    def remove_vertex(self, vertex): 
        if vertex in self.adj_list.keys(): 
            for vertex_edge in self.adj_list[vertex]: 
                self.adj_list[vertex_edge].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False




my_grapg = Graph()
my_grapg.add_vertex("A")
my_grapg.add_vertex("B")
my_grapg.add_vertex("C")
my_grapg.add_vertex("D")

my_grapg.add_edge("A", "B")
my_grapg.add_edge("C", "A")
my_grapg.add_edge("A", "D")
my_grapg.add_edge("C", "D")
my_grapg.add_edge("B", "D")

my_grapg.print_graph()

print("remove vertex")

my_grapg.remove_vertex("D")
my_grapg.print_graph()

