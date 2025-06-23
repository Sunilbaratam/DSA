class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

def kruskal(graph):
    # Get all the vertices in the graph
    vertices = set()
    for edge in graph:
        vertices.add(edge[0])
        vertices.add(edge[1])
    
    # Initialize the disjoint set
    disjoint_set = DisjointSet(vertices)
    
    # Sort edges by their weights
    edges = sorted(graph, key=lambda edge: edge[2])
    
    mst = []
    total_cost = 0
    
    for edge in edges:
        vertex1, vertex2, weight = edge
        root1 = disjoint_set.find(vertex1)
        root2 = disjoint_set.find(vertex2)
        
        # If root1 and root2 are different, the edge does not form a cycle
        if root1 != root2:
            mst.append(edge)
            total_cost += weight
            disjoint_set.union(root1, root2)
    
    return mst, total_cost

# Example graph represented as a list of edges (vertex1, vertex2, weight)
graph = [
    ('A', 'B', 4),
    ('A', 'H', 8),
    ('B', 'H', 11),
    ('B', 'C', 8),
    ('C', 'D', 7),
    ('C', 'I', 2),
    ('C', 'F', 4),
    ('D', 'E', 9),
    ('D', 'F', 14),
    ('E', 'F', 10),
    ('F', 'G', 2),
    ('G', 'H', 1),
    ('G', 'I', 6),
    ('H', 'I', 7)
]

# Running Kruskal's algorithm
mst, total_cost = kruskal(graph)
print("Edges in MST:", mst)
print("Total cost of MST:", total_cost)
