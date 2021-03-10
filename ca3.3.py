import math
INF = math.inf
class Edge:
    def __init__(self,_id):
        self.edge_id = _id
        self.connections = {}
        
    def add_yaal_to_edge(self,edge_id,number):
        self.connections[edge_id] = number
    
    def __repr__(self):
        return(str(self.edge_id)+ " "+ str(self.connections))
    
class Graph:
    def __init__(self,n):
        self.edges = []
        self.num_of_edges = n
        self.make_edges()
        self.paths = []
        self.set_paths()

    def set_paths(self):
        for i in range(self.num_of_edges + 1):
            self.paths.append(INF)
        self.paths[0] = 0

    def make_edges(self):
        for i in range(self.num_of_edges + 1):
            new_edge = Edge(i)
            self.edges.append(new_edge)
        for i in range(len(self.edges) - 1):
            self.edges[i].add_yaal_to_edge(i+1,2*(10**9))
            if i <len(self.edges) - 2:
                self.edges[i+1].add_yaal_to_edge(i,0)
            else:
                self.edges[i+1].add_yaal_to_edge(i,-1)
    
    def add_yaal(self,begin_edge,end_edge,number):
        self.edges[begin_edge].add_yaal_to_edge(end_edge,number)
    
    def __repr__(self):
        return str(self.edges)
            
    def print_an_example(self):  
        print("Yes") 
        line = "" 
        for i in range(1,self.num_of_edges+1):  
            line +=(str(self.paths[i] - self.paths[i-1]) + " ")
        print(line)
      
    def cycle_found(self):
        for first_edge in self.edges:
            for second_edge in first_edge.connections:
                if self.paths[first_edge.edge_id] + first_edge.connections[second_edge] < self.paths[second_edge]:  
                    return True
        return False

    def shoul_be_updated(self,first_edge,edge_2_id):
        edge_1_id = first_edge.edge_id
        if self.paths[edge_1_id] + first_edge.connections[edge_2_id] < self.paths[edge_2_id]:  
            return True
        return False
    
    def find_paths(self):  
          
        for _ in range(self.num_of_edges - 1):  
            for first_edge in self.edges:
                edge_1_id = first_edge.edge_id
                for edge_2_id in first_edge.connections:
                    if self.shoul_be_updated(first_edge,edge_2_id) == True:  
                        self.paths[edge_2_id] = self.paths[edge_1_id] + first_edge.connections[edge_2_id]  

        if self.cycle_found() == True:
            print("No") 
        else:
            self.print_an_example()

n_m = input().strip().split()
n = int(n_m[0])
m = int(n_m[1])
graph = Graph(n)
done = False
for i in range(m):
    lessthan = None
    morethan = None
    line = input()
    if ">" in line:
        line = line.split(">")
        morethan = int(line[1])  
    elif "<" in line:
        line = line.split("<")
        lessthan = int(line[1])
    nums = [int(x) for x in line[0].split("-")]
    if nums[1] == n and lessthan == 1:
        print("No")
        done = True
        break
    if lessthan != None:
        graph.add_yaal(nums[0]-1,nums[1],lessthan - 1)
    else:
        graph.add_yaal(nums[1],nums[0] - 1,-morethan - 1)
if done == False:
    graph.find_paths()