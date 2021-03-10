INF  = 10 ** 10

class Handle_Visitings:
    def __init__(self,num_of_families):
        self.families = []
        self.num_of_families = num_of_families
        self.visitings = []
        self.make_init_families()
        self.visit_duration = 0
        self.answers = []
                    
    def make_init_families(self):
        for i in range(self.num_of_families):
            new_family = Family(i+1)
            self.families.append(new_family)
    
    def set_k(self,k):
        self.visit_duration = k
            
    def add_visit(self,begin_family,end_family):
        self.visitings.append([begin_family,end_family])

    def calculate_end_time(self,visit):
        begin_family = self.families[visit[0] - 1]
        end_family = self.families[visit[1] - 1]
        route_length = self.dist[begin_family.family_id - 1][end_family.family_id - 1]
        visiting_begin = max( (begin_family.can_leave_home_at + route_length) , end_family.arrive_home_at )
        begin_family.arrive_home_at = visiting_begin + route_length + self.visit_duration
        begin_family.can_leave_home_at = begin_family.arrive_home_at
        end_family.can_leave_home_at = max(visiting_begin + self.visit_duration,end_family.can_leave_home_at)
        self.answers.append(visiting_begin + self.visit_duration)
        
    def set_shortest_paths(self,graph):
        self.dist = [[0 for i in range(self.num_of_families)] for j in range(self.num_of_families)]
        for i in range(self.num_of_families):
            for j in range(self.num_of_families):
                self.dist[i][j] = graph[i][j]
      
        for k in range(self.num_of_families): 
            for i in range(self.num_of_families): 
                for j in range(self.num_of_families): 
                    if self.dist[i][j] > self.dist[i][k] + self.dist[k][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]

    def set_answers(self):
        for visit in self.visitings:
            self.calculate_end_time(visit)
    
    def print_answers(self):
        for ans in self.answers:
            print(ans)
            
class Family:
    def __init__(self,_id):
        self.family_id = _id
        self.arrive_home_at = 0
        self.can_leave_home_at = 0
    def add_route(self,family_id,route_length):
        self.routes.append([family_id,route_length])

n_m = [int(x) for x in input().split()]
n = n_m[0]
m = n_m[1]
handle_visitings = Handle_Visitings(n)
paths = [[INF for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            paths[i][j] = 0
            
for i in range(m):
    numbers = [int(x) for x in input().split()]
    first_edge = numbers[0]
    second_edge = numbers[1]
    length = numbers[2]  
    if first_edge != second_edge:
        if paths[first_edge-1][second_edge-1] > length:
            paths[first_edge-1][second_edge-1] = length  
            paths[second_edge-1][first_edge-1] = length  

handle_visitings.set_shortest_paths(paths)
q_k = [int(x) for x in input().split()]
q = q_k[0]
k = q_k[1]
handle_visitings.set_k(k)

for i in range(q):
    visiting = [int(x) for x in input().split()]
    ai = visiting[0]
    bi = visiting[1]
    handle_visitings.add_visit(ai,bi)

handle_visitings.set_answers()
handle_visitings.print_answers()