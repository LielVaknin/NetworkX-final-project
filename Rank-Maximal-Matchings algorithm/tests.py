import unittest
import networkx as nx
import rank_maximal_matching as rmm


class rank_maximal_matching(unittest.TestCase):
    def check_match(self):
        # example1
        matching = {('a1', 'p2'), ('a3', 'p4'), ('a1', 'p1')}
        G = nx.Graph()
        # Add nodes with the node attribute 'bipartite'
        G.add_nodes_from(['a1', 'a2', 'a3', 'a4'], bipartite=0)
        G.add_nodes_from(['p1', 'p2', 'p3', 'p4'], bipartite=1)
        # Add edges only between nodes of opposite node sets
        G.add_weighted_edges_from([('a1', 'p1', 1), ('a1', 'p2', 1), ('a2', 'p2', 1), ('a2', 'p3', 2), ('a3', 'p4', 1)])
        # our function
        M = rmm.rank_maximal_matching(G) 

        self.assertEqual(M, matching)

        # example2
        matching = {('a1', 'p2')}
        G.add_nodes_from(['a1', 'a2'], bipartite=0)
        G.add_nodes_from(['p1', 'p2'], bipartite=1)
        G.add_weighted_edges_from([('a1', 'p1', 2), ('a1', 'p2', 1), ('a2', 'p2', 2)])
        # our function
        M = rmm.rank_maximal_matching(G)
        self.assertEqual(M, matching)

        # example3
        matching = {('a1', 'p1'), ('a2', 'p2')}
        G.add_nodes_from(['a1', 'a2'], bipartite=0)
        G.add_nodes_from(['p1', 'p2'], bipartite=1)
        G.add_weighted_edges_from([('a1', 'p1', 1), ('a1', 'p2', 2), ('a2', 'p2', 1), ('a3', 'p2', 1)])
        # our function
        M = rmm.rank_maximal_matching(G)
        self.assertEqual(M, matching)


if __name__ == '__main__':
    unittest.main()
