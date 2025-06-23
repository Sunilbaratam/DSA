import heapq

class PriorityQueue():
    def __init__(self) -> None:
        self.elements = []

    def is_empty(self):
        return len(self.elements)==0
    
    def put(self, item, priority):
        heapq.heappush(self.elements,(priority, item ))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def prim(graph, start_vertex):
    visited = set()
    priority_queue = PriorityQueue()
    mst = []
    total_cost = 0 
    priority_queue = priority_queue.put(start_vertex, 0)

    edge_to = {start_vertex: (None, 0)}

    while not priority_queue.is_empty():
        current_vertex = priority_queue.get()
        if current_vertex  in visited:
            continue

        visited.add(current_vertex)
        parent_vertex, weight = edge_to[current_vertex][0], edge_to[current_vertex][1]
        if parent_vertex is not None:
            mst.append((parent_vertex, current_vertex, weight))
            total_cost += weight
        
        for neighbour, neighbour_weight in graph[current_vertex]:
            if neighbour not in visited:
                if neighbour not in edge_to or neighbour_weight<edge_to[neighbour][1]:
                    edge_to[neighbour] = (current_vertex, neighbour_weight)
                    priority_queue.put(neighbour,neighbour_weight)
        
        return mst, total_cost

    