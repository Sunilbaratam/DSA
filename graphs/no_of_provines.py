def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        def bfs(visited, adj_list, v):
            q = []
            q.append(v)
            visited[v] = 1
            while q:
                j = q.pop(0)
                for k in adj_list[j]:
                    if visited[k] != 1:
                        visited[k] = 1
                        q.append(k)
        
        vertices = len(isConnected)

        adj_list = [[] for _ in range(vertices)]

        for i in range(vertices):
            for j in range(vertices):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)
        
        visited = [0 for i in range(vertices)]

        c = 0
        for i in range(vertices):
            if visited[i]==0:
                c+=1
                bfs(visited, adj_list, i)
        return c
