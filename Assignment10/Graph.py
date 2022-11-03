class Graph:
    adjacency: list;

    def __init__(self, nodes: int) -> None:
        self.adjacency = [[] for i in range(nodes)];

    def addEdge(self, start, end):
        if(not self.adjacency[start].count(end)):
            self.adjacency[start].append(end);
            self.adjacency[start].sort();

    def __str__(self):
        output = "";
        for node in range(len(self.adjacency)):
            output += f"N{node}:\t";
            for edge in self.adjacency[node]:
                output += f"{edge}, ";
            output += "\n";
        return output;

myGraph = [ [0,  1], [1, 2], [2, 9], [3,  2],
            [3,  4], [4, 5], [4, 6], [4,  7], 
            [6,  7], [7, 8], [9, 8], [9, 10], 
            [11, 2]];

graph = Graph(12);
for edge in range(len(myGraph)):
    graph.addEdge(myGraph[edge][0], myGraph[edge][1]);
print(graph);
