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
            # ��steps[i]������һ�������node�����ģ���parent֮�����С��step��
            # ���������step��Ӧ�õ���level��
            # ����������������steps[i]��һ��С�ڸ�node��level������˵�����node��֮ǰĳ����parent
            # ��node�����������γ���һ������
            # �����Ļ�������������connection�Ͳ���critical connection
            steps[v] = level + 1
            
            for child in graph[v]:
                # edge case������parent
                if child == parent:
                    continue
                # unexplored node
                # �������node��stepֵ�����child��ĳ��֮ǰ��node�������γ�һ������
                # ��ôparentҲ��
                elif steps[child] == -1:
                    steps[v] = min(steps[v], dfs(child, v, level+1, steps, result, graph))
                else:
                    steps[v] = min(steps[v], steps[child])
            # step[i]�������node��level+1
            # ���vΪ0����ʱv��parent��-1��������һ��dummy node��������Ҫ�ų���v==0
            if steps[v] == level + 1 and v != 0:
                result.append([parent, v])
            return steps[v]
        
        result = []
        dfs(0, -1, 0, steps, result, graph)
        return result