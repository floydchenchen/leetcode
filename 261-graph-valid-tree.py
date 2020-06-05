# 261. Graph Valid Tree

# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.
#
# Example 1:
#
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# Example 2:
#
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1]
# is the same as [1,0] and thus will not appear together in edges.

# 思路：
# 1. 如果是一个tree，那么 边数 = 节点数 - 1

from collections import defaultdict


class Solution:
    # 1. BFS solution: 找cycle
    def validTree(self, n, edges):
        # 如果是一个tree，那么 边数 = 节点数 - 1
        if len(edges) != n - 1:
            return False

        neighbors = defaultdict(list)
        for [u, v] in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        visited, q = set(), [0]
        parents = [-1] * n

        while q:
            u = q.pop(0)
            visited.add(u)

            for v in neighbors[u]:
                # already visited v, so v should be the parent of u
                if v in visited and parents[u] != v:
                    return False
                if v not in visited:
                    q.append(v)
                    parents[v] = u
        return len(visited) == n

    # 2. DFS solution
    def validTree1(self, n, edges):
        if len(edges) != n - 1:
            return False

        neighbors = {i: [] for i in range(n)}
        for [u, v] in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        def visit(v):
            list(map(visit, neighbors.pop(v, [])))
        visit(0)
        return not neighbors

    # 3. union find solution
    def validTree2(self, n, edges):
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(x):
            return x if parent[x] == x else find(parent[x])

        for edge in edges:
            [u, v] = list(map(find, edge))
            if u == v:
                return False
            parent[u] = v

        return True


print(Solution().validTree(5, [[1, 4], [0, 1], [0, 2], [0, 3]]))
