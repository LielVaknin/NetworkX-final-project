
import networkx as nx







if __name__ == '__main__':
    matching = {('a2', 'p2'), ('a3', 'p4'), ('a1', 'p1')}
    B = nx.Graph()
    # Add nodes with the node attribute "bipartite"
    B.add_nodes_from(["a1", "a2", "a3", "a4"], bipartite=0)
    B.add_nodes_from(["p1", "p2", "p3", "p4"], bipartite=1)
    G = nx.DiGraph()
    G.add_edge("A", "C")
    G.add_edge("A", "B")
    G.add_edge("C", "E")
    G.add_edge("C", "D")
    G.add_edge("E", "G")
    G.add_edge("E", "F")
    G.add_edge("G", "I")
    G.add_edge("G", "H")
    print(nx.bipartite.hopcroft_karp_matching(G))




