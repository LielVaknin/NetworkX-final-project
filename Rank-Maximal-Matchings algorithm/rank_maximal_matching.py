"""
Returns the rank maximal matching of the ranked bipartite graph `G`.

    A ranked graph is a grpah wich every edge has a rank [1,r] such that 1
    is the highest rank, and then 2 is the highest rank, and so 1.

    A matching is a set of edges that do not share any nodes.

    A rank-maximal matching is one in which the maximum
    possible number of edges with first rank, and subject to that condition,
    the maximum possible number of edges with second rank, and so on.

    Parameters
    ----------
    G : NetworkX graph

      Undirected wheighted (ranked) bipartite graph

    Returns
    -------
    M : dictionary

      The matching is returned as a dictionary, `M`, such that
      M contains ``(u, v)`` edges in the matching .


    Raises
    ------


    Notes
    -----
    This function is implemented with the `Hopcroft--Karp matching algorithm
    <https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm>`_ for
    bipartite graphs.

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

##################################################
"""
Gi - is a graph with i' ranked edges 
return- EVi - set of even vretices
        Oi - set of odd vertices
        Ui - set of unreachable vertices
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