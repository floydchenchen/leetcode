# 133. Clone Graph

# Given the head of a graph, return a deep copy (clone) of the graph.
# Each node in the graph contains a label (int) and a list (List[UndirectedGraphNode]) of its neighbors.
# There is an edge between the given node and each of the nodes in its neighbors.
#
#
# OJ's undirected graph serialization (so you can understand error output):
# Nodes are labeled uniquely.
#
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
#
#
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
#
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
#
#
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
# Note: The information about the tree serialization is only meant so that
# you can understand error output if you get a wrong answer.
# You don't need to understand the serialization to solve the problem.

# Definition for a undirected graph node
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # DFS
    def __init__(self):
        self.dic = dict()
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        # exit
        if node.val in self.dic:
            return self.dic[node.val]
    
        clone = Node(node.val)
        self.dic[node.val] = clone
        for neighbor in node.neighbors:
            new_neighbor = self.cloneGraph(neighbor)
            clone.neighbors.append(new_neighbor)
        return clone

    # iterative DFS using a stack
    def cloneGraph1(self, node):
        if not node:
            return node
        root = UndirectedGraphNode(node.label)
        stack = [node]
        dic = dict()
        dic[node.label] = root
        while stack:
            top = stack.pop()

            for n in top.neighbors:
                if n.label not in dic:
                    stack.append(n)
                    dic[n.label] = UndirectedGraphNode(n.label)
                dic[top.label].neighbors.append(dic[n.label])

        return root

    # BFS solution using a queue
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        root = Node(node.val)
        # visited
        dic = dict()
        dic[node.val] = root
        q = [node]
        while q:
            n = q.pop(0)
            for neighbor in n.neighbors:
                # # neighbor is not visited
                if neighbor.val not in dic:
                    q.append(neighbor)
                    dic[neighbor.val] = Node(neighbor.val)
                dic[n.val].neighbors.append(dic[neighbor.val])
        return root
