

class Solution:
    def isBipartite(self, graph) -> bool:
        for i in range(len(graph)):
            if len(graph[i]) == 0:
                return False
#ad
        A = set()
        B = set()
        visited = set()

        stack = []

        stack.append(0)
        last_team_a = False
        # while stack is not empty
        while len(stack) != 0:
            current_node = stack[-1]

            if current_node not in visited:
                visited.add(current_node)
                if last_team_a:
                    B.add(current_node)
                    last_team_a = False
                else:
                    A.add(current_node)
                    last_team_a = True

            neighbor_node = None

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    neighbor_node = neighbor
                    stack.append(neighbor_node)
                    break
            if neighbor_node == None:
                stack.pop()

        for a_node in A:
            for i in graph[a_node]:
                if i in A:
                    return False

        for b_node in B:
            for j in graph[b_node]:
                if j in B:
                    return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isBipartite([[4],[],[4],[4],[0,2,3]]))
