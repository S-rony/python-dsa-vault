from collections import deque


class Graph:
    def __init__(self, vertex):
        self.mat = [[0]*vertex for _ in range(vertex)]
        self.size = vertex

    def add_edge(self, src, dest):
        #undirectional edge
        if (0 <= src < self.size) and (0 <= dest < self.size):
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else:
            print("Invalid Edge")
        # directional edge
        # if (0 <= src < self.size) and (0 <= dest < self.size):
        #     self.mat[src][dest] = 1

        # weighted edge
        # if (0 <= src < self.size) and (0 <= dest < self.size):
        #     self.mat[src][dest] = 3

    def BFS(self,src):
        visited = [False] * self.size
        #v=visited
        # '*' means repetition operator
        queue = deque([src])
        visited[src] = True

        while queue:
            v = queue.popleft()
            print(v, end=" ")

            for i in range(self.size):
                if self.mat[v][i] == 1 and visited[i] == False:
                    visited[i] = True
                    queue.append(i)

G = Graph(8)
G.add_edge(0,1)
G.add_edge(0,3)
G.add_edge(1,3)
G.add_edge(3,5)
G.add_edge(3,4)
G.add_edge(4,5)
G.add_edge(4,6)
G.add_edge(6,2)
G.add_edge(6,7)

G.BFS(0)





