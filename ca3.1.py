class Yaal:
    def __init__(self,num,bn,en):
        self.number = num
        self.begin_node = bn
        self.end_node = en
        self.zero_one = 1
    def __repr__(self):
        return str(self.number)
class Tree:
    def __init__(self,n,input_matrix):
        self.Yaals = []
        self.num_of_nodes = n
        self.consoles = 0
        self.input_matrix = input_matrix
        self.parents = []
        self.ranks = []
        self.set_parents_and_ranks()
        
    def add_yaal(self,num,beginnode,endnode):
        self.input_matrix[beginnode][endnode] = num
        if self.input_matrix[endnode][beginnode] != -1:
            if self.input_matrix[endnode][beginnode] >= num:
                new_yaal = Yaal(num,beginnode,endnode)
                self.Yaals.append(new_yaal)
                if self.input_matrix[endnode][beginnode] == num:     
                    new_yaal = Yaal(num,endnode,beginnode)
                    self.Yaals.append(new_yaal)
            else:
                new_yaal = Yaal(self.input_matrix[endnode][beginnode],endnode,beginnode)
                self.Yaals.append(new_yaal)
                
    def sort_yaals(self,input_matrix):
        self.Yaals.sort(key = lambda x:x.number)
        
    def find(self, i): 
        while self.parents[i] != i:
            i = self.parents[i]
        return i
                
    def union(self,a,b): 
        a_root = self.find(a) 
        b_root = self.find(b) 

        if self.ranks[a_root] < self.ranks[b_root]: 
            self.parents[a_root] = b_root 
        elif self.ranks[a_root] > self.ranks[b_root]: 
            self.parents[b_root] = a_root 

        else : 
            self.parents[b_root] = a_root 
            self.ranks[a_root] += 1
     
    def make_temp_list(self,i) :
        counter = i
        temp_list = [self.Yaals[counter]]
        while counter < len(self.Yaals) - 1:
            if self.Yaals[counter].number == self.Yaals[counter + 1].number:
                temp_list.append(self.Yaals[counter + 1])
            else:
                break
            counter += 1
        return temp_list
    
    def set_parents_and_ranks(self):
        for i in range(self.num_of_nodes): 
            self.parents.append(i) 
            self.ranks.append(0) 
            
    def find_MST(self,sum_of_all_yaals): 
        is_empty = True
        i = 0 
        num_of_included_edges = 0 
                        
        sum_of_included_yaals = 0
        
        while num_of_included_edges < self.num_of_nodes - 1: 
            temp_list = self.make_temp_list(i)
            if is_empty == True:
                for yaal in temp_list:
                    yaal.zero_one = 0
                    a = self.find(yaal.begin_node) 
                    b = self.find(yaal.end_node) 
                    if a != b:
                        num_of_included_edges += 1    
                        self.union(a, b)             
                        sum_of_included_yaals += yaal.number
                        is_empty = False
                        i += 1
            else:
                a_to_be_added = 0
                b_to_be_added = 0
                yaal_to_be_added = None
                added = False
                for yaal in temp_list:
                    a = self.find(yaal.begin_node) 
                    b = self.find(yaal.end_node) 
                    if a != b:
                        yaal.zero_one = 0
                        if added == False:
                            a_to_be_added = a
                            b_to_be_added = b
                            added = True
                            yaal_to_be_added = yaal
                        
                if added == True:
                    num_of_included_edges += 1
                    self.union(a_to_be_added,b_to_be_added)
                    sum_of_included_yaals += yaal_to_be_added.number
                    
                i += 1                    

        final = sum_of_all_yaals - sum_of_included_yaals
        self.consoles = final

    def print_answer(self,input_matrix,sum_of_all_yaals):
        ans = [[1 for i in range(n)] for j in range(n)]
        for i in range(len(self.Yaals)):
            begin = self.Yaals[i].begin_node
            end = self.Yaals[i].end_node
            if  self.Yaals[i].zero_one == 0:
                ans[begin][end] = 0
                
        print(self.consoles)

        for i in range(n):
            line = ""
            for j in range(n):
                line += str(ans[i][j]) + " "
            print(line)


n_c = input().strip().split()
n = int(n_c[0])
c = int(n_c[1])
sum_of_all_yaals = 0
input_matrix = [[-1 for i in range(n)] for j in range(n)]
tree = Tree(n,input_matrix)

for i in range(n):
    numbers = [int(x) for x in input().strip().split()]
    for j in range(len(numbers)):
        sum_of_all_yaals += numbers[j]
        if i != j:
            tree.add_yaal(numbers[j],i,j)
        
tree.sort_yaals(input_matrix)
tree.find_MST(sum_of_all_yaals)
tree.print_answer(input_matrix,sum_of_all_yaals)