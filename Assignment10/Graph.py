class Graph:
    matrix: list;
    nodes: int;

    def __init__(self, nodes: int) -> None:
        self.matrix = [[0]*nodes for i in range(nodes)];
        self.nodes= len(self.matrix);

    def __str__(self):
        output = "\t";
        for node in range(len(self.matrix)):
            extraSpace = " " * (3 - len(str(node)));
            output += f"{node}{extraSpace}"; 
        output += "\n";

        for node in range(len(self.matrix)):
            output += f"N{node}:\t";
            for edge in range(len(self.matrix[node])):
                output += f"{self.matrix[node][edge]}, ";
            output += "\n";
        return output;

    ########################################
    # Setting up graph functions
    ########################################

    def isValidNode(self, node: int):
        if(node < 0 or node >= self.nodes):
            print(f"Node {node} does not exist");
            return False;

        return True;

    #Check for param errors
    def addEdge(self, start, end):
        if(self.isValidNode(start) and self.isValidNode(end)):
            self.matrix[start][end] = 1;

    #Check for param errors
    def delEdge(self, start, end):
        if(self.isValidNode(start) and self.isValidNode(end)):
            self.matrix[start][end] = 0;

    ########################################
    # Searching and sorting functions
    ########################################

    def dfs(self, current, visited, dfsVisited):
        visited[current] = True;
        for nextNode in range(self.nodes):
            if(not visited[nextNode] and self.matrix[current][nextNode]):
                self.dfs(nextNode, visited, dfsVisited);
        dfsVisited.append(current);

    def topSort(self):
        visited = [False]*(self.nodes);
        order = [0]*(self.nodes);
        i = self.nodes - 1;

        for current in range(self.nodes):
            if(not visited[current]):
                dfsVisited = [];
                self.dfs(current, visited, dfsVisited);
                for node in dfsVisited:
                    order[i] = node;
                    i -= 1;
        return order;



#######################################
# Other Functions for question #3
#######################################

def dfs(graph: Graph, start: int):
    print(f"{start} -> ", end="");
    if(not graph.isValidNode(start)):
        return;
    # Iterate through all possible edges between nodes
    for nextNode in range(len(graph.matrix)):
        # If edge exist, run recursion
        if(graph.matrix[start][nextNode]):
            dfs(graph, nextNode);

def bfs(graph: Graph, startNodes: list):
    print(f"{startNodes} -> ", end="");
    nextLayer = [];
    # Iterate through all nodes in current layer
    for start in startNodes:
        if(not graph.isValidNode(start)):
           continue;
        # Iterate through all possible edges
        for nextNode in range(len(graph.matrix)):
            # If edge exist, add to list 
            if(graph.matrix[start][nextNode]):
                nextLayer.append(nextNode);
    # Call for next layer if there is one
    if(len(nextLayer)):
        bfs(graph, nextLayer);



#######################################
# Function for part 4?
#######################################

def scc(graph: Graph):
    sort = graph.topSort();
    assigned = [False]*graph.nodes;
    groups = [];

    # go through each node in graph 
    for node in sort:
        # only add to group if not in group
        if(not assigned[node]):
            groups.append(assign(graph, assigned, node));

    return groups;

# Returns a list of lists of connect parts
def assign(graph, assigned, start) -> list:
   group = [start];
   assigned[start] = True;
   for inEdge in range(graph.nodes):
       if(not assigned[inEdge] and graph.matrix[inEdge][start]):
           group += assign(graph, assigned, inEdge);
   return group;


#######################################
# Testing output
#######################################

myGraph = [ [0,  1], [1, 2], [2, 9], [3,  2],
            [3,  4], [4, 5], [4, 6], [4,  7], 
            [6,  7], [7, 8], [9, 8], [9, 10], 
            [11, 2]];

graph = Graph(12);
for edge in range(len(myGraph)):
    graph.addEdge(myGraph[edge][0], myGraph[edge][1]);

print("\nBreadth First Search on node 3");
bfs(graph, [3]);
print("\nBreadth First Search on node 0");
bfs(graph, [0]);
print("\nBreadth First Search on node 24 (doesn't exist)");
bfs(graph, [24]);

print("\nDepth First Search on node 3");
dfs(graph, 3);
print("\nDepth First Search on node 0");
dfs(graph, 0);
print("\nDepth First Search on node 24 (doesn't exist)");
dfs(graph, 24);

print(f"\nTopological Sort on graph");
print(f"{graph.topSort()}");
print(f"\nStrongly connected component groups");
print(f"{scc(graph)}\n");

