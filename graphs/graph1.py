# graph from Goodrich

class Graph:
    """Simple graph using adjacency map"""
    
    # Nested Vertex class
    class Vertex:
        """Lightweight vertex component"""
        __slots__ = '_element'

        def __init__(self, x):
            self._element = x
        
        def element(self):
            return self._element            # Element of vertex

        def __hash__(self):                 # Make vertex map/set
            return hash(id(self))

        def __str__(self):
            return str(self._element)

    # Nested Edge class
    class Edge:
        """Lightweight edge component"""
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            return(self._origin, self._destination)

        def opposite(self, v):
            """Return vertex that is opposite v on this edge"""
            if not isinstance(v, Graph.Vertex):
                raise TypeError('v must be a Vertex')
            return self._destination if v is self._origin else self._origin
            raise ValueError('v not incident to edge')

        def element(self):
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0},{1},{2})'.format(self._origin, self._destination, self._element)
    
    # Graph methods
    def __init__(self, directed=False):
        """Default empty, undirected graph constructor"""
        self._outgoing = {}

        # create second map for directed graph
        self._incoming = {} if directed else self._outgoing

    def _validate_vertex(self, v):
        # verify v is a vertex of this graph
        if not isinstance(v, self.Vertex):
            raise TypeError('Vertex expected')
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def is_directed(self):
        """True if directed"""
        return self._incoming is not self._outgoing

    def vertex_count(self):
        """Number of vertices in graph"""
        return len(self._outgoing)

    def vertices(self):
        """Iteration of all vertices"""
        return self._outgoing.keys()

    def edge_count(self):
        """Number of edges"""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs ensure double count of edges
        return total if self.is_directed() else total // 2

    def edges(self):
        """A set of edges of the graph"""
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        """Edge from u to v or None if not adjacent"""
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        """Number of outgoing edges incodent to vertex v"""
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """All outgoing edges incident to vertex v"""
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new vertex with element x"""
        v = self.Vertex(x)
        self._outgoing[v] = [v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v 

    def insert_edge(self, u, v, x=None):
        """Insert and return a new edge from u to v with auxilary element x"""
        if self.get_edge(u, v) is not None:
            raise ValueError("u and v are already adjacent")
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[u][v] = e

if __name__ == "__main__":
    g = Graph()