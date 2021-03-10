import math
class Yaal:
    def __init__(self,begin,end,num):
        self.begin_node = begin
        self.end_node = end
        self.number = num

class Graph:
    def __init__(self,n):
        self.Yaals = []
        self.num_of_edges = n
        self.deleted_yaals = []
        
    def add_yaal(self,begin,end,num):
        new_yaal = Yaal(begin,end,num)
        self.Yaals.append(new_yaal)
        if num == 0:
            self.deleted_yaals.append(new_yaal)
    
    def print_ans(self):
        print("No")
    def dijkstra(self): 
        self.print_ans()
    
n_m_k = [int(x) for x in input().strip().split()]
n = n_m_k[0]
m = n_m_k[1]
k = n_m_k[2]
graph = Graph(n)
for i in range(m):
    v_u_w = [int(x) for x in input().strip().split()]
    v = v_u_w[0]
    u = v_u_w[1]
    w = v_u_w[2]
    graph.add_yaal(v,u,w)

d = int(input().strip())
graph.dijkstra()
