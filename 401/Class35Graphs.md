# Graphs

In this module, we will be learning about Graphs. Graphs are essentially a data structure that take the concept of connecting nodes one step further. The first node based implementation we studied was linked lists where each node could be connected to only one node (either singly or doubly). The next implementation was with binary or k-ary trees in which there is one root node that is linked to two or more (with a consistent maximum) amount of nodes in one direction. Something linked lists and k-ary trees had in common was a head or root or some starter node that nothing else is linked to. 

While graphs share nodes and edges, graphs are non-linear. Graphs can be directed (which is to say you can only travel in one direction along an edge between two points) or undirected (in which you can move in either direction between two points).

- There are complete graphs where every point is connected to every other point, connected graphs where every point is at least connected to something or disconnected graphs that can have points without any references to other points. 
- There are cyclic graphs where through traversing the graph, you can end up at the starter node, or acyclic graphs where this does not happen. Note that these would need to be directed graphs.

Graphs can be represented with matrices that show which points are connected to which other points. They can be traversed using stacks to analyze through the vertices and connections. While graph traversals can be used for applications such as GPS Navigation, there are further applications of this problem such as with solving the [Traveling Salesman Problem](https://towardsdatascience.com/how-to-solve-the-traveling-salesman-problem-a-comparative-analysis-39056a916c9f) which is currently solved only up to 22 cities. 

To learn more, check out the source I referenced on [Graphs](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-35/resources/graphs.html)!

[Reading Notes Home Page](README.md)