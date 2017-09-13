# Runtime: 82ms Beats or equals to 86%
from Y2017.UndirectedGraphNode import UndirectedGraphNode



class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        neighbors = {}
        nodes = {}
        res=node.label
        def addNode(_node):
            if _node.label in neighbors:
                return
            neighbors[_node.label] = [n.label for n in _node.neighbors]
            for n in _node.neighbors:
                addNode(n)

        addNode(node)
        for k in neighbors.keys():
            nodes[k] = UndirectedGraphNode(k)
        for k in neighbors.keys():
            nodes[k].neighbors = [nodes[n] for n in neighbors[k]] if neighbors[k] else []
        return nodes[res]
node1=UndirectedGraphNode(-1)
node2=UndirectedGraphNode(1)
node1.neighbors=[node2]






solution = Solution()
print(solution.cloneGraph(node1))

