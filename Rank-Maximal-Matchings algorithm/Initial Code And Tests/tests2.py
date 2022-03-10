import collections
import unittest
from itertools import count

import networkx as nx
import rank_maximal_matching as rmm
import copy


def G1():  # graph from example number 1
    G = nx.Graph()
    G.add_nodes_from(["a1", "a2"], bipartite=0)
    G.add_nodes_from(["p1", "p2"], bipartite=1)
    G.add_weighted_edges_from(
        [('a1', 'p1', 2), ('a1', 'p2', 1), ('a2', 'p2', 2)])
    return G


def G2():  # graph from example number 2
    G = nx.Graph()
    G.add_nodes_from(["a1", "a2", "a3"], bipartite=0)
    G.add_nodes_from(["p1", "p2"], bipartite=1)
    G.add_weighted_edges_from(
        [('a1', 'p1', 1), ('a1', 'p2', 2), ('a2', 'p2', 1), ('a3', 'p1', 1)])
    return G


def G3():  # graph from example number 3
    G = nx.Graph()
    G.add_nodes_from(["a1", "a2", "a3"], bipartite=0)
    G.add_nodes_from(["p1", "p2", "p3"], bipartite=1)
    G.add_weighted_edges_from(
        [('a1', 'p2', 2), ('a1', 'p3', 3), ('a2', 'p2', 3), ('a3', 'p1', 2), ('a3', 'p2', 3)])
    return G


def G4():  # graph from example number 4
    G = nx.Graph()
    G.add_nodes_from(["a1", "a2", "a3", "a4", "a5"], bipartite=0)
    G.add_nodes_from(["p1", "p2", "p3", "p4", "p5", "p6"], bipartite=1)
    G.add_weighted_edges_from(
        [('a1', 'p1', 1), ('a1', 'p2', 3), ('a1', 'p3', 2), ('a2', 'p3', 1), ('a2', 'p4', 2), ('a2', 'p5', 3)
            , ('a3', 'p5', 1), ('a3', 'p6', 2), ('a4', 'p4', 1)
            , ('a5', 'p2', 2), ('a5', 'p4', 1), ('a5', 'p5', 4), ('a5', 'p6', 3)])
    return G


def article_graph():
    B = nx.Graph()  # example from the article figure 3
    B.add_nodes_from(["a1", "a2", "a3"], bipartite=0)
    B.add_nodes_from(["p1", "p2", "p3"], bipartite=1)
    B.add_weighted_edges_from(
        [('a1', 'p1', 1), ('a1', 'p2', 1)
            , ('a2', 'p1', 2), ('a2', 'p2', 1), ('a2', 'p3', 2)
            , ('a3', 'p2', 2), ('a3', 'p1', 1)])
    # B.add_weighted_edges_from(
    #     [('a1', 'p1', 1), ('a1', 'p2', 1)
    #     , ('a2', 'p2', 1)
    #         , ('a3', 'p1', 1)])
    return B


class MyTestCase(unittest.TestCase):
    def test_rmm(self):
        G= article_graph()
        top_nodes = ["a1", "a2", "a3"]
        #print(rmm.rank_maximal_matching(G,rank="weight",top_nodes=top_nodes))

        G = G1()
        top_nodes = ["a1", "a2"]
        M =rmm.rank_maximal_matching(G, rank="weight", top_nodes=top_nodes)
        counts_of_ranks = collections.Counter(G[node][M[node]]["weight"] for node in M)
        self.assertEqual({1: 2},counts_of_ranks)

        G = G2()
        top_nodes =["a1", "a2", "a3"]
        M = rmm.rank_maximal_matching(G, rank="weight", top_nodes=top_nodes)
        counts_of_ranks = collections.Counter(G[node][M[node]]["weight"] for node in M)
        self.assertEqual({1: 4},counts_of_ranks)

        G= G3()
        top_nodes=["a1", "a2", "a3"]
        M = rmm.rank_maximal_matching(G, rank="weight", top_nodes=top_nodes)
        counts_of_ranks = collections.Counter(G[node][M[node]]["weight"] for node in M)
        self.assertEqual({2: 4},counts_of_ranks)

        G = G4()
        top_nodes = ["a1", "a2", "a3", "a4", "a5"]
        M = rmm.rank_maximal_matching(G, rank="weight", top_nodes=top_nodes)
        counts_of_ranks = collections.Counter(G[node][M[node]]["weight"] for node in M)
        self.assertEqual({1: 8, 2: 2},counts_of_ranks)

        """graph = nx.Graph(G)
        Gi = nx.Graph()
        Gi.add_nodes_from(G.nodes)
        max_rank, min_rank = rmm.get_max_and_min_rank(G, rank="weight")
        rmm.create_Gi(graph, Gi, min_rank, rank="weight")
        left, right = rmm.bipartite_sets(G, top_nodes)
        M = {'a1':'p1', 'a2':'p2', 'p1':'a1', 'p2':'a2'}
        free_nodes = rmm.find_free_vertices(Gi, M)
        print(free_nodes)
        for i in range(min_rank, max_rank):
            even, odd, unreachable = rmm.divide_to_sets(Gi, M, free_nodes)
            print(even,odd,unreachable)
            rmm.remove_edges(graph, odd, unreachable, i, rank="weight")
            # remove_OO_edges(Gi, odd)
            # remove_OU_edges(Gi, odd, unreachable)
            rmm.create_Gi(graph, Gi, i + 1, rank="weight")
            print(Gi.edges)
            #M = rmm.get_mi_plus1(Gi, M, free_nodes)
            M = nx.bipartite.hopcroft_karp_matching(Gi,top_nodes=top_nodes)
        print(M)"""


    def test_max_aum_path(self):
        G = G1()  # nx.Graph
        M = {"a1": "p2", "p2": "a1"}
        self.assertEqual({'a1': 'p2', 'p2': 'a1'},rmm.max_augmenting_path(G,M,["a2","p1","p2","a1"]))
        G = G2()
        M = {"a1": "p1", "p1": "a1"}

    def test_divide_to_set(self):
        G = G1()
        matched_edges = {"a1": "p2", "p2": "a1"}
        G.remove_edges_from([(u, v, d) for (u, v, d) in G.edges(data=True) if d["weight"] > 1])
        self.assertEqual(rmm.alternating_dfs(G, matched_edges, ["a2", "p1"]), ({'a2', 'p1'}, set(), {'a1', 'p2'}))
        G = G2()
        matched_edges = {"a1": "p1", "p1": "a1", "a2": "p2", "p2": "a2"}
        G.remove_edges_from([(u, v, d) for (u, v, d) in G.edges(data=True) if d["weight"] > 1])
        self.assertEqual(rmm.divide_to_sets(G, matched_edges, ["a3"]), ({'a1', 'a3'}, {'p1'}, {'a2', 'p2'}))
        G = G3()
        matched_edges = {"a1": "p2", "p2": "a1", "a3": "p1", "p1": "a3"}
        G.remove_edges_from([(u, v, d) for (u, v, d) in G.edges(data=True) if d["weight"] > 2])
        self.assertEqual(rmm.divide_to_sets(G, matched_edges, ["a2", "p3"]),
                         ({'p3', 'a2'}, set(), {'a3', 'a1', 'p1', 'p2'}))
        G = G4()
        matched_edges = {"a1": "p1", "p1": "a1", "a2": "p3", "p3": "a2", "a3": "p5", "p5": "a3"
            , "a4": "p4", "p4": "a4", "a5": "p2", "p2": "a5"}
        G.remove_edges_from([(u, v, d) for (u, v, d) in G.edges(data=True) if d["weight"] > 1])
        self.assertEqual(rmm.divide_to_sets(G, matched_edges, ["p6"]),
                         ({'p6'}, set(), {'p1', 'a2', 'p4', 'p5', 'a5', 'a3', 'p2', 'a1', 'p3', 'a4'}))
        G = article_graph()
        matched_edges = {"a1": "p1", "p1": "a1", "a2": "p2", "p2": "a2"}
        G.remove_edges_from([(u, v, d) for (u, v, d) in G.edges(data=True) if d["weight"] > 1])
        self.assertEqual(rmm.divide_to_sets(G, matched_edges, ["a3", "p3"]),
                         ({'p3', 'a1', 'a2', 'a3'}, {'p1', 'p2'}, set())),
        ({'a3', 'a1', 'a2', 'p3'}, {'p2', 'p1'}, set())

    def test_find_free_vertices(self):
        G = G1()
        matched_edges = {'a1': 'p2', 'p2': 'a1'}
        self.assertEqual(['a2', 'p1'], rmm.find_free_vertices(G, matched_edges))
        G = G2()
        matched_edges = {"a1": "p1", "p1": "a1", "a2": "p2", "p2": "a2"}
        self.assertEqual(['a3'], rmm.find_free_vertices(G, matched_edges))
        G = G3()
        matched_edges = {"a1": "p2", "p2": "a1", "a3": "p1", "p1": "a3"}
        self.assertEqual(['a2', 'p3'], rmm.find_free_vertices(G, matched_edges))
        G = G4()
        matched_edges = {"a1": "p1", "p1": "a1", "a2": "p3", "p3": "a2", "a3": "p5", "p5": "a3"
            , "a4": "p4", "p4": "a4", "a5": "p2", "p2": "a5"}
        self.assertEqual(['p6'], rmm.find_free_vertices(G, matched_edges))

    def test_remove_edges(self):
        G = nx.Graph()  # big example
        G.add_nodes_from(["a1", "a2", "a3", "a4"], bipartite=0)
        G.add_nodes_from(["p1", "p2", "p3", "p4", "p5"], bipartite=1)
        G.add_weighted_edges_from(
            [('a1', 'p1', 1), ('a1', 'p2', 1), ('a1', 'p3', 3), ('a1', 'p5', 2)
                , ('a2', 'p1', 1), ('a2', 'p2', 2), ('a2', 'p3', 2)
                , ('a3', 'p2', 1), ('a3', 'p4', 2), ('a3', 'p5', 1)
                , ('a4', 'p3', 2), ('a4', 'p4', 3), ('a4', 'p5', 1)])
        o, u = {"p1", "p2", "p5"}, {}
        graph = copy.deepcopy(G)
        rmm.remove_edges(graph, o, u, 1, rank="weight")
        removed_edges = [(u, v) for (u, v) in G.edges if (u, v) not in graph.edges]
        self.assertEqual(removed_edges, [('a1', 'p5'), ('a2', 'p2')])
        B = article_graph()  # example from article figure 3
        graph = copy.deepcopy(B)
        rmm.remove_edges(graph, {"p1", "p2"}, {}, 1, rank="weight")
        removed_edges = [(u, v) for (u, v) in B.edges if (u, v) not in graph.edges]
        self.assertEqual([('a2', 'p1'), ('a3', 'p2')], removed_edges)


if __name__ == '__main__':
    unittest.main()
