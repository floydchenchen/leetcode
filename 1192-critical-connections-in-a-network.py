# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.
#
# A critical connection is a connection that, if removed, will make some server unable to reach some other server.
#
# Return all critical connections in the network in any order.

# Example 1:
#               2 
#            /  |  
#           1 - 0
#           | ==> critical connection
#           3
#
# 
# 
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
import collections
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # make graph: a map of set
        graph = collections.defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        # initialize rank list
        steps = [-1] * n
        
        # starting from the current node, explore all the node connecting to the node except for its parent,
        # and return the minimum value node
        def dfs(v: int, parent: int, level: int, steps: list, result: list, graph) -> int:
            # 用steps[i]来储存一个和这个node相连的，除parent之外的最小的step数
            # 正常情况下step数应该等于level数
            # 但是如果相连的这个steps[i]是一个小于该node的level的数，说明这个node和之前某个非parent
            # 的node相连，这里形成了一个环。
            # 这样的话，这个环里面的connection就不是critical connection
            steps[v] = level + 1
            
            for child in graph[v]:
                # edge case，跳过parent
                if child == parent:
                    continue
                # unexplored node
                # 更新这个node的step值，如果child和某个之前的node相连能形成一个环，
                # 那么parent也能
                elif steps[child] == -1:
                    steps[v] = min(steps[v], dfs(child, v, level+1, steps, result, graph))
                else:
                    steps[v] = min(steps[v], steps[child])
            # step[i]等于这个node的level+1
            # 如果v为0，这时v的parent是-1，这里是一个dummy node，所以需要排除掉v==0
            if steps[v] == level + 1 and v != 0:
                result.append([parent, v])
            return steps[v]
        
        result = []
        dfs(0, -1, 0, steps, result, graph)
        return result