"""
Returns the rank maximal matching of the ranked bipartite graph `G`.

    A ranked graph is a graph in which every edge has a rank [1,r] such that 1
    is the highest rank, and then 2 is the next highest rank, and so on.

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


        >>> G = nx.DiGraph()
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

        >>> G = nx.DiGraph()
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


def rank_maximal_matching(G):
    M = {}
    
    return M


"""
Gi - is a graph with i' ranked edges 
return- EVi - set of even vretices
        Oi  -  set of odd vertices
        Ui  -  set of unreachable vertices
"""


"""def divide_to_sets(Gi):
    return EVi, Oi, Ui


def divide_vertices_by_rank(G):
    return {}
"""

"""
Gi - is a graph with i' ranked edges
return - list_of_free_vertices 
"""


"""def find_free_vertices(Gi):
    return list_of_free_vertices


def create_Gi_plus_1(Gi, rank):
    return Gi


def get_G1(G):
    return G1"""


# def remove_OO_edges(G,Oi):
#     return
#
# def remove_OU_edges(G,Oi,Ui):
#     return
"""
remove edges from Oi or Ui with rank greater than rank_i 
remove OiUi edges
remove OiOi edges
"""


"""def remove_edges(G, Oi, Ui, rank_i):
    return


def get_reverse_of_augmenting_path(Gi):
    return augmenting_path"""

