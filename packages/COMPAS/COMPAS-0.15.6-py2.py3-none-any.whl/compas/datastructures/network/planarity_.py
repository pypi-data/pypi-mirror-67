from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from math import cos
from math import sin
from math import pi

import planarity

from compas.geometry import angle_vectors_xy
from compas.geometry import is_intersection_segment_segment_xy
from compas.geometry import is_ccw_xy
from compas.geometry import subtract_vectors_xy


__all__ = [
    'network_is_crossed',
    'network_count_crossings',
    'network_find_crossings',
    'network_is_xy',
    'network_is_planar',
    'network_is_planar_embedding',
    'network_embed_in_plane',
]


def network_is_crossed(network):
    """Verify if a network has crossing edges.

    Parameters
    ----------
    network : Network
        A network object.

    Returns
    -------
    bool
        True if the network has at least one pair of crossing edges.
        False otherwise.

    Notes
    -----
    This algorithm assumes that the network lies in the XY plane.

    """
    for u1, v1 in network.edges():
        for u2, v2 in network.edges():
            if u1 == u2 or v1 == v2 or u1 == v2 or u2 == v1:
                continue
            else:
                a = network.node_attributes(u1, 'xy')
                b = network.node_attributes(v1, 'xy')
                c = network.node_attributes(u2, 'xy')
                d = network.node_attributes(v2, 'xy')
                if is_intersection_segment_segment_xy((a, b), (c, d)):
                    return True
    return False


def _are_edges_crossed(edges, vertices):
    for u1, v1 in edges:
        for u2, v2 in edges:
            if u1 == u2 or v1 == v2 or u1 == v2 or u2 == v1:
                continue
            else:
                a = vertices[u1]
                b = vertices[v1]
                c = vertices[u2]
                d = vertices[v2]
                if is_intersection_segment_segment_xy((a, b), (c, d)):
                    return True
    return False


def network_count_crossings(network):
    """Count the number of crossings (pairs of crossing edges) in the network.

    Parameters
    ----------
    network : Network
        A network object.

    Returns
    -------
    int
        The number of crossings.

    Notes
    -----
    This algorithm assumes that the network lies in the XY plane.

    """
    return len(network_find_crossings(network))


def network_find_crossings(network):
    """Identify all pairs of crossing edges in a network.

    Parameters
    ----------
    network : Network
        A network object.

    Returns
    -------
    list
        A list of edge pairs, with each edge represented by two vertex keys.

    Notes
    -----
    This algorithm assumes that the network lies in the XY plane.

    """
    crossings = set()
    for u1, v1 in network.edges():
        for u2, v2 in network.edges():
            if u1 == u2 or v1 == v2 or u1 == v2 or u2 == v1:
                continue
            else:
                if ((u1, v1), (u2, v2)) in crossings:
                    continue
                if ((u2, v2), (u1, v1)) in crossings:
                    continue
                a = network.node_attributes(u1, 'xy')
                b = network.node_attributes(v1, 'xy')
                c = network.node_attributes(u2, 'xy')
                d = network.node_attributes(v2, 'xy')
                if is_intersection_segment_segment_xy((a, b), (c, d)):
                    crossings.add(((u1, v1), (u2, v2)))
    return list(crossings)


def network_is_xy(network):
    """Verify that a network lies in the XY plane.

    Parameters
    ----------
    network : Network
        A network object.

    Returns
    -------
    bool
        True if the Z coordinate of all vertices is zero.
        False otherwise.

    """
    z = None
    for key in network.nodes():
        if z is None:
            z = network.node_attribute(key, 'z') or 0.0
        else:
            if z != network.node_attribute(key, 'z') or 0.0:
                return False
    return True


def network_is_planar(network):
    """Check if the network is planar.

    Parameters
    ----------
    network : Network
        A network object.

    Returns
    -------
    bool
        True if the network is planar.
        False otherwise.

    Raises
    ------
    ImportError
        If the planarity package is not installed.

    Notes
    -----
    A network is planar if it can be drawn in the plane without crossing edges.
    If a network is planar, it can be shown that an embedding of the network in
    the plane exists, and, furthermore, that straight-line embedding in the plane
    exists.

    Warning
    -------
    This function uses the python binding of the *edge addition planarity suite*.
    It is available on Anaconda: https://anaconda.org/conda-forge/python-planarity.

    Examples
    --------
    >>>
    """
    return planarity.is_planar(list(network.edges()))


def network_is_planar_embedding(network):
    """Verify that a network is embedded in the plane without crossing edges.

    Parameters
    ----------
    network : Network
        A network object.

    Returns
    -------
    bool
        True if the network is embedded in the plane without crossing edges.
        Fase otherwise.

    """
    return (network_is_planar(network) and
            network_is_xy(network) and not
            network_is_crossed(network))


def network_embed_in_plane(network, fix=None, straightline=True):
    """Embed the network in the plane.

    Parameters
    ----------
    network : Network
        A network object.
    fix : list (None)
        Two fixed points.
    straightline : bool (True)
        Embed using straight lines.

    Returns
    -------
    bool
        True if the embedding was successful.
        False otherwise.

    Raises
    ------
    ImportError
        If NetworkX is not installed.

    Warning
    -------
    This function uses the Python package NetworkX. NetworkX can be *pip installed*.

    Examples
    --------
    >>>
    """
    try:
        import networkx as nx
    except ImportError:
        print("NetworkX is not installed. Get NetworkX at https://networkx.github.io/.")
        raise

    x = network.vertices_attribute('x')
    y = network.vertices_attribute('y')
    xmin, xmax = min(x), max(x)
    ymin, ymax = min(y), max(y)
    xspan = xmax - xmin
    yspan = ymax - ymin

    edges = [(u, v) for u, v in network.edges() if not network.is_vertex_leaf(u) and not network.is_vertex_leaf(v)]

    is_embedded = False

    count = 100
    while count:
        graph = nx.Graph(edges)
        pos = nx.spring_layout(graph, 2, iterations=100, scale=max(xspan, yspan))
        if not _are_edges_crossed(edges, pos):
            is_embedded = True
            break
        count -= 1

    if not is_embedded:
        return False

    if fix:
        a, b = fix
        p0 = network.node_attributes(a, 'xy')
        p1 = network.node_attributes(b, 'xy')
        p2 = pos[b]
        vec0 = subtract_vectors_xy(p1, p0)
        vec1 = subtract_vectors_xy(pos[b], pos[a])
        # rotate
        a = angle_vectors_xy(vec0, vec1)
        if is_ccw_xy(p0, p1, p2):
            a = 2 * pi - a
        cosa = cos(a)
        sina = sin(a)
        for key in pos:
            x, y = pos[key]
            pos[key][0] = cosa * x - sina * y
            pos[key][1] = sina * x + cosa * y
        # scale
        l0 = (vec0[0] ** 2 + vec0[1] ** 2) ** 0.5
        l1 = (vec1[0] ** 2 + vec1[1] ** 2) ** 0.5
        scale = l0 / l1
        for key in pos:
            pos[key][0] *= scale
            pos[key][1] *= scale
        # translate
        t = subtract_vectors_xy(p0, pos[a])
        for key in pos:
            pos[key][0] += t[0]
            pos[key][1] += t[1]

    # update network vertex coordinates
    for key in network.vertices():
        if key in pos:
            network.node_attributes(key, 'xy', pos[key])

    return True


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    import compas

    from compas.datastructures import Network
    from compas_plotters import NetworkPlotter

    network = Network.from_obj(compas.get('lines.obj'))

    network.add_edge(6, 15)

    if not network_is_planar(network):
        crossings = network_find_crossings(network)
    else:
        crossings = []

    print(crossings)

    plotter = NetworkPlotter(network, figsize=(8, 5))
    plotter.defaults['node.fontsize'] = 6

    plotter.draw_nodes(radius=0.15, text={key: key for key in network.nodes()})
    plotter.draw_edges(color={edge: '#ff0000' for edges in crossings for edge in edges})

    plotter.show()
