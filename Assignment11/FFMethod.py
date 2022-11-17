

########################################
# Graph class for performing FFMethod on
########################################

class Graph(object):
    matrix: list;
    nodes: int;

    def __init__(self, nodes):
        self.nodes = abs(nodes);
        self.matrix = [[0]*nodes for i in range(nodes)];

    def setEdge(self, start, end, weight):
        self.matrix[start][end] = weight;

    def subEdge(self, start, end, weight):
        self.matrix[start][end] -= weight;

    def delEdge(self, start, end):
        self.matrix[start][end] = 0;

    def __str__(self):
        out = " ";
        letters = ['s', 't', 'a', 'b', 'c', 'd'];
        for letter in letters:
            out += f" {letter}";
        for start in range(len(self.matrix)):
            out += f"\n{letters[start]} ";
            for end in range(len(self.matrix)):
                out += f"{self.matrix[start][end]} ";

        return out;



########################################
# Functions 
########################################

def Ford(graph: Graph):
    # Setting up graphs
    flow = Graph(g.nodes);
    res = Graph(g.nodes);
    # Copy values from g into residual
    for start in range(len(graph.matrix)):
        for end in range(len(graph.matrix[start])):
            res.setEdge(start, end, graph.matrix[start][end]);

    # Setup aug path to have just the first path
    # from source to sink
    augPath = dfs(res, 0, 1);
    augPath = augPath[0:augPath.index(1)+1];

    while (len(augPath) > 1):
        # Get max flow
        maxFlow = res.matrix[augPath[0]][augPath[1]];
        for node in range(len(augPath)-1):
            if (maxFlow > res.matrix[augPath[node]][augPath[node+1]]):
                maxFlow = res.matrix[augPath[node]][augPath[node+1]];

        for node in range(len(augPath)-1):
            # Add path with max flow to flow
            flow.matrix[augPath[node]][augPath[node+1]] += maxFlow;
            # Subtract path with max flow from res
            res.matrix[augPath[node]][augPath[node+1]] -= maxFlow;

        # Next aug path
        augPath = dfs(res, 0, 1);
        if (not augPath.count(1)):
            break;
        augPath = augPath[0:augPath.index(1)+1];

    return flow;

# Returns all paths starting from start that end at end
def dfs(g: Graph, start, end):
    if (start == end):
        return [end];

    path = [start];
    for edge in range(g.nodes):
        if (g.matrix[start][edge]):
            path += dfs(g, edge, end);

    if (path[len(path)-1] == end):
        return path;
    else:
        return [];

########################################
# Testing stuff
########################################

#Order  s, t, a, b, c, d
#       0, 1, 2, 3, 4, 5
gData = [[0, 2, 4], [0, 3, 2], [4, 1, 3], [5, 1, 3],
         [2, 3, 1], [2, 4, 2], [2, 5, 4], [3, 5, 2]];

g = Graph(6);
for data in gData:
    g.setEdge(data[0], data[1], data[2]);

print(f"\nMaximum flow based on graph from assignment as a weighted adjacency matrix\n");
print(Ford(g));
print();
