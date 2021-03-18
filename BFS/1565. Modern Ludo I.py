# App1: use defaultdict to store source: dests. bfs. if connected and visited[node] < visited[connected_node], then 
# enqueue connected node again.
class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """

    def modernLudo(self, length, connections):
        if not length:
            return 0

        data, q, visited = collections.defaultdict(list), collections.deque([1]), {1: 0}
        for source, dest in connections:
            data[source].append(dest)

        while q:
            node = q.popleft()
            if node in data:
                connected_nodes = data[node]
                for connected_node in connected_nodes:
                    if connected_node not in visited or visited[node] < visited[connected_node]:
                        visited[connected_node] = visited[node]
                        q.append(connected_node)

            for i in range(1, 7):
                new_node = node + i
                if new_node > length:
                    break
                # if new_node in visited and visited[new_node] <= visited[node] + 1:
                #     continue
                # q.append(new_node)
                # visited[new_node] = visited[node] + 1
                if new_node not in visited or new_node in visited and visited[node] + 1 < visited[new_node]:
                    q.append(new_node)
                    visited[new_node] = visited[node] + 1

        return visited[length]
