# Graphs

A graph is a set of objects called `vertices`, together with a collection of pairwise connections between them called `edges`. It is a way or representing relationships between pairs of objects.

The vertices are also called nodes while the edges are also called arcs. The edges can be described as `directed` if they are ordered and `undirected` if they are not ordered, and `unidirected` if all edges are undirected.

Practical examples of graphs are city maps, electrical wiring mappings,

## Terminologies

- Vertices are the nones
- Edges eonnects two nodes
- Paths are a sequence of nodes for moving around the graph

## Types of graphs

There are three types of graphs: undirected graphs, directed graphs, and weighted graphs

## Disioint Set Operations

This can be implemented with Find and Union operations.

## Starting with a simple directed graph

```python
G = (
    {1,2,3,4},
    {(1,2), (1,3), (1,4)},
)
```

The graph G has 4 vertices v and 3 edges e. It is represented pictorially as 4 labeled circles (vertices) with 3 lines (edges)
