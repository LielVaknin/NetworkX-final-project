import collections
import copy
import math

import networkx as nx
from networkx.algorithms.bipartite import sets as bipartite_sets

"""
Returns the rank maximal matching of the ranked bipartite graph `G`.
    A ranked graph is a graph in which every edge has a rank [1,r]
    (the algorithm ignores non-positive ranks)
    such that 1 is the highest rank, and then 2 is the next highest rank, and so on.
    A matching is a set of edges that do not share any nodes.
    A rank-maximal matching is one with the maximum
    possible number of edges with the first rank, and subject to that condition,
    the maximum possible number of edges with the second rank, and so on.
    Parameters
    ----------
    G : NetworkX graph
      Undirected weighted (the weight of every edge represents the rank) bipartite graph
    Returns
    -------
    M : dictionary
       The matching is returned as a dictionary, `matching`, such that
         ``matching[v] == w`` if node `v` is matched to node `w`. Unmatched
        nodes do not occur as a key in `matching`.
    Examples
    --------
    In the biaprtite graph, G = (V,E). with the sets V1 as 0 and V2 as 1,
    and the weight of the edges as the ranks.
        >>> G = nx.Graph()
        >>> G.add_nodes_from(['a1', 'a2'], bipartite=0)
        >>> G.add_nodes_from(['p1', 'p2'], bipartite=1)
        >>> G.add_weighted_edges_from([('a1', 'p1', 2), ('a1', 'p2', 1), ('a2', 'p2', 2)])
        >>> M=nx.rank_maximal_matching(G)
        >>> print(M)
        {'a1': 'p2', 'p2': 'a1'}
        >>>m['a1']
        'p2'
        explanation:                            2
                        G =             a1-----------p1
                                         \
                                          \
                                           \
                                            \
                                             \ 1
                                              \
                                               \
                                                \
                                           2     \
                                    a2-----------p2
         The matching M1 is {'a1':'p2', 'p2':'a1'} so O1, EV1 and U1 are  {a1,p2},{a2,p1},{} respectively.
         After removing the edges incident to O1 with the rank higher than 1 {(a1,p1),(a2,p2)} there are no more edges
         to add to G1, so an augmenting path doesnt exists and the algorithm ends returning M1.
        -------
        >>> G = nx.Graph()
        >>> G.add_nodes_from(['a1', 'a2', 'a3'], bipartite=0)
        >>> G.add_nodes_from(['p1', 'p2'], bipartite=1)
        >>> G.add_weighted_edges_from([('a1', 'p1', 1), ('a1', 'p2', 2), ('a2', 'p2', 1), ('a3', 'p2', 1)])
        >>> M=nx.rank_maximal_matching(G)
        >>> print(M)
        {'a1': 'p1', 'a2': 'p2', 'p1': 'a1', 'p2': 'a2'}
        >>> m['a1']
        'p1'
    Raises
    ------
    AmbiguousSolution
      Raised if the input bipartite graph is disconnected and no container
      with all nodes in one bipartite set is provided. When determining
      the nodes in each bipartite set more than one valid solution is
      possible if the input graph is disconnected.
    Notes
    -----
    This function uses the algorithm published in the article of Irving et al. (2006), "Rank maximal matching".
    See :mod:`bipartite documentation <networkx.algorithms.bipartite>`
    for further details on how bipartite graphs are handled in NetworkX.
    See Also
    --------
    maximum_matching
    hopcroft_karp_matching
    References
    ----------
    Irving, Robert W. and Kavitha, Telikepalli and Mehlhorn, Kurt and Michail, Dimitrios and Paluch, Katarzyna E.,
    "Rank-Maximal Matchings",ACM Trans. Algorithms,2006,Association for Computing Machinery**
       https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.92.6742&rep=rep1&type=pdf
    """


def rank_maximal_matching(G, rank="rank", top_nodes=None):
    Gi = get_G1(G, rank=rank)
    left, right = bipartite_sets(G, top_nodes)
    M = nx.bipartite.hopcroft_karp_matching(Gi, top_nodes)
    free_nodes = find_free_vertices(Gi, M)
    graph = nx.Graph(G)
    max_rank = get_max_rank(G, rank)
    for i in range(1, max_rank):
        even, odd, unreachable = divide_to_sets(Gi, M, free_nodes)
        remove_edges(graph, odd, unreachable, i, rank=rank)
        remove_OO_edges(Gi, odd)
        remove_OU_edges(Gi, odd, unreachable)
        create_Gi_plus_1(graph, Gi, i, rank=rank)
        M = get_mi_plus1(G, M, free_nodes)
    return M


def get_max_rank(G, rank="rank"):
    return max([d[rank] for (u, v, d) in G.edges(data=True)])


def get_mi_plus1(G, M, free_nodes):
    return max_augmenting_path(G, M, free_nodes)


def max_augmenting_path(G, M, free_nodes):
    matched_edges = [(k, v) for k, v in M.items()]
    paths = [{}]
    max_sym_matching = M
    max_length_sym_matching = len(matched_edges)
    for u in free_nodes:
        visited = set()
        initial_depth = 0
        stack = [(u, iter(G[u]), initial_depth, {})]
        visited.add(u)
        while stack:
            parent, children, depth, path = stack[-1]
            try:
                child = next(children)
                if child not in visited:
                    current_symmetric_matching = copy.deepcopy(path)
                    if depth % 2 == 0 and (parent, child) not in matched_edges:
                        current_symmetric_matching[parent] = child
                        if child in free_nodes:
                            paths.append(current_symmetric_matching)
                            if len(current_symmetric_matching) > max_length_sym_matching:
                                max_length_sym_matching = len(current_symmetric_matching)
                                max_sym_matching = current_symmetric_matching
                        else:
                            visited.add(child)
                            stack.append((child, iter(G[child]), depth + 1,current_symmetric_matching))
                    elif depth % 2 == 1 and (parent, child) in matched_edges:
                        visited.add(child)
                        stack.append((child, iter(G[child]), depth + 1, current_symmetric_matching))
            except StopIteration:
                stack.pop()
    return max_sym_matching


def alternating_dfs(G, matched_edges, free_nodes):
    """Returns True if and only if `u` is connected to one of the
    targets by an alternating path.
    `u` is a vertex in the graph `G`.
    If `along_matched` is True, this step of the depth-first search
    will continue only through edges in the given matching. Otherwise, it
    will continue only through edges *not* in the given matching.
    """
    even = set()
    odd = set()
    unreachable = set(G.nodes)
    visited = set()
    for u in free_nodes:
        if u in visited:
            continue
        initial_depth = 0
        stack = [(u, iter(G[u]), initial_depth)]
        even.add(u)
        unreachable.remove(u)
        visited.add(u)
        while stack:
            parent, children, depth = stack[-1]
            try:
                child = next(children)
                if child not in visited:
                    if depth % 2 == 0 and (parent, child) not in matched_edges:
                        odd.add(child)
                        visited.add(child)
                        unreachable.remove(child)
                        stack.append((child, iter(G[child]), depth + 1))
                    elif depth % 2 == 1 and (parent, child) in matched_edges:
                        even.add(child)
                        visited.add(child)
                        unreachable.remove(child)
                        stack.append((child, iter(G[child]), depth + 1))
            except StopIteration:
                stack.pop()
    return even, odd, unreachable


"""
Gi - is a graph with i' ranked edges 
return- EVi - set of even vretices
        Oi  -  set of odd vertices
        Ui  -  set of unreachable vertices
"""


def divide_to_sets(Gi, M, free_nodes):
    matched_edges = [(k, v) for k, v in M.items()]
    # unmatched_edges = [(k, v) for k, v in Gi.edges(data=True) if (k, v) not in matched_edges]
    return alternating_dfs(Gi, matched_edges, free_nodes)


"""
Gi - is a graph with i' ranked edges
return - list_of_free_vertices 
"""


def find_free_vertices(Gi: nx.Graph, M):
    free_nodes = list(Gi.nodes)
    for key in M:
        free_nodes.remove(key)
    return free_nodes


def create_Gi_plus_1(G, Gi, rank_i, rank="rank"):
    Gi.add_edges_from([(u, v, d) for (u, v, d) in G.edges(data=True) if d[rank] == rank_i + 1])


def get_G1(G: nx.Graph, rank="rank"):
    G1 = nx.Graph()
    G1.add_nodes_from(G.nodes)
    G1.add_edges_from([(u, v, d) for (u, v, d) in G.edges(data=True) if d[rank] == 1])
    return G1


def remove_OO_edges(G, Oi):
    G.remove_edges_from([(u, v) for (u, v) in G.edges if
                         (u in Oi and v in Oi)])


def remove_OU_edges(G, Oi, Ui):
    G.remove_edges_from([(u, v) for (u, v) in G.edges if
                         (u in Oi and v in Ui) or (v in Oi and u in Ui)])


"""
remove edges from Oi or Ui with rank greater than rank_i 
remove OiUi edges
remove OiOi edges
"""


def remove_edges(G, Oi, Ui, rank_i, rank="rank"):
    G.remove_edges_from([(u, v) for (u, v, d) in G.edges(data=True) if
                         d[rank] > rank_i and (u in Oi or v in Oi or u in Ui or v in Ui)])
