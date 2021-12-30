import unittest
import networkx as nx
import rank_maximal_matching as rmm


class rank_maximal_matching(unittest.TestCase):
    def test_rank_maximal_matching_bigger_left(self):
        G=nx.Graph()
        matching = {'a1': 'p1', 'a2': 'p2', 'p1': 'a1', 'p2': 'a2'}
        G.add_nodes_from(['a1', 'a2', 'a3'], bipartite=0)
        G.add_nodes_from(['p1', 'p2'], bipartite=1)
        G.add_weighted_edges_from([('a1', 'p1', 1), ('a1', 'p2', 2), ('a2', 'p2', 1), ('a3', 'p2', 1)])
        # our function
        M = rmm.rank_maximal_matching(G)
        self.assertEqual(M, matching)

    def test_rank_maximal_matching_bigger_right(self):
        matching = {'a1': 'p2', 'a3': 'p4', 'a2': 'p1', 'p2': 'a1', 'p4': 'a3', 'p1': 'a2'}
        G = nx.Graph()
        # Add nodes with the node attribute 'bipartite'
        G.add_nodes_from(['a1', 'a2', 'a3'], bipartite=0)
        G.add_nodes_from(['p1', 'p2', 'p3', 'p4'], bipartite=1)
        # Add edges only between nodes of opposite node sets
        G.add_weighted_edges_from([('a1', 'p1', 1), ('a1', 'p2', 1), ('a2', 'p2', 1), ('a2', 'p3', 2), ('a3', 'p4', 1)])
        # our function
        M = rmm.rank_maximal_matching(G, rank="weight")
        self.assertEqual(M, matching)

    def test_rank_maximal_matching_same_size(self):
        matching = {'a1': 'p2', 'a3': 'p1', 'p2': 'a1','p1': 'a3'}
        G = nx.Graph()
        # Add nodes with the node attribute 'bipartite'
        G.add_nodes_from(['a1', 'a2', 'a3'], bipartite=0)
        G.add_nodes_from(['p1', 'p2', 'p3'], bipartite=1)
        # Add edges only between nodes of opposite node sets
        G.add_weighted_edges_from([('a1', 'p2', 1), ('a1', 'p3', 2), ('a2', 'p2', 2), ('a3', 'p1', 1), ('a3', 'p2', 2)])
        # our function
        M = rmm.rank_maximal_matching(G,rank="weight")
        self.assertEqual(M, matching)

    def test_rank_maximal_matching_disconnected_graph(self):
        matching = {'a1': 'p2', 'a2': 'p1', 'a3': 'p5', 'a4': 'p3',
                    'p2': 'a1', 'p1': 'a2', 'p5': 'a3', 'p3': 'a4'}
        G = nx.Graph()
        G.add_nodes_from(['a1', 'a2', 'a3','a4','a5'], bipartite=0)
        G.add_nodes_from(['p1', 'p2', 'p3','p4','p5'], bipartite=1)
        G.add_weighted_edges_from([('a1', 'p1', 1), ('a1', 'p2', 1), ('a1', 'p5', 2),
                                   ('a2', 'p1', 1), ('a2', 'p2', 2),('a2', 'p3', 2),
                                   ('a3', 'p2', 1),('a3', 'p4', 2),('a3', 'p5', 1),
                                   ('a4', 'p3', 2),('a4', 'p4', 3),('a4', 'p5', 2)])


        M = rmm.rank_maximal_matching(G, rank="weight")
        self.assertEqual(M, matching)


    # should throw an exception
    # ignore
    def test_rank_maximal_matching_negative_rank(self):
        G = nx.Graph()

    def test_rank_maximal_matching_perfect_matching(self):
        matching = {'a1': 'p2', 'a3': 'p1', 'a2': 'p3', 'p2': 'a1', 'p1': 'a3', 'p3': 'a2'}
        G = nx.Graph()
        # Add nodes with the node attribute 'bipartite'
        G.add_nodes_from(['a1', 'a2', 'a3'], bipartite=0)
        G.add_nodes_from(['p1', 'p2', 'p3'], bipartite=1)
        # Add edges only between nodes of opposite node sets
        G.add_weighted_edges_from(
            [('a1', 'p2', 1), ('a1', 'p3', 2), ('a2', 'p2', 2), ('a3', 'p1', 1), ('a3', 'p2', 2), ('a2', 'p3', 1)])
        # our function
        M = rmm.rank_maximal_matching(G, rank="weight")
        self.assertEqual(M, matching)

    def test_rank_maximal_matching_unordered_ranks(self):
        matching = {'a1': 'p2', 'a3': 'p1', 'p2': 'a1','p1': 'a3'}
        G = nx.Graph()
        # Add nodes with the node attribute 'bipartite'
        G.add_nodes_from(['a1', 'a2', 'a3'], bipartite=0)
        G.add_nodes_from(['p1', 'p2', 'p3'], bipartite=1)
        # Add edges only between nodes of opposite node sets
        G.add_weighted_edges_from([('a1', 'p2', 1), ('a1', 'p3', 3), ('a2', 'p2', 4), ('a3', 'p1', 2), ('a3', 'p2', 3)])
        # our function
        M = rmm.rank_maximal_matching(G, rank="weight")
        self.assertEqual(M, matching)



    def check_match(self):
        # example1
        matching = {'a1': 'p2', 'a3': 'p4', 'a2': 'p1','p2': 'a1', 'p4': 'a3','p1':'a2'}
        G = nx.Graph()
        # Add nodes with the node attribute 'bipartite'
        G.add_nodes_from(['a1', 'a2', 'a3'], bipartite=0)
        G.add_nodes_from(['p1', 'p2', 'p3', 'p4'], bipartite=1)
        # Add edges only between nodes of opposite node sets
        G.add_weighted_edges_from([('a1', 'p1', 1), ('a1', 'p2', 1), ('a2', 'p2', 1), ('a2', 'p3', 2), ('a3', 'p4', 1)])
        # our function
        M = rmm.rank_maximal_matching(G)

        self.assertEqual(M, matching)

        # example2
        G.clear()
        matching = {'a1': 'p2', 'p2': 'a1'}
        G.add_nodes_from(['a1', 'a2'], bipartite=0)
        G.add_nodes_from(['p1', 'p2'], bipartite=1)
        G.add_weighted_edges_from([('a1', 'p1', 2), ('a1', 'p2', 1), ('a2', 'p2', 2)])
        # our function
        M = rmm.rank_maximal_matching(G)
        self.assertEqual(M, matching)

        # example3
        G.clear()
        matching = {'a1': 'p1', 'a2': 'p2', 'p1': 'a1', 'p2':'a2'}
        G.add_nodes_from(['a1', 'a2','a3'], bipartite=0)
        G.add_nodes_from(['p1', 'p2'], bipartite=1)
        G.add_weighted_edges_from([('a1', 'p1', 1), ('a1', 'p2', 2), ('a2', 'p2', 1), ('a3', 'p2', 1)])
        # our function
        M = rmm.rank_maximal_matching(G)
        self.assertEqual(M, matching)

        G = nx.Graph()
        G.add_nodes_from(['a1', 'a2', 'a3', 'a4'], bipartite=0)
        G.add_nodes_from(['p1', 'p2', 'p3', 'p4', 'p5'], bipartite=1)
        G.add_weighted_edges_from([('a1', 'p1', 1), ('a1', 'p2', 1), ('a1', 'p5', 2),
                                   ('a2', 'p1', 1), ('a2', 'p2', 2), ('a2', 'p3', 2),
                                   ('a3', 'p2', 1), ('a3', 'p4', 2), ('a3', 'p5', 1),
                                   ('a4', 'p3', 2), ('a4', 'p4', 3), ('a4', 'p5', 2)])
        matching = {'a1': 'p2', 'a2': 'p1', 'a3': 'p5', 'a4': 'p3',
                    'p2': 'a1', 'p1': 'a2', 'p5': 'a3', 'p3': 'a4'}

        M = rmm.rank_maximal_matching(G, rank="weight")
        self.assertEqual(M, matching)


if __name__ == '__main__':
    unittest.main()
