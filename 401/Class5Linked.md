# Linked Lists and The Traveling Salesman

A **linked list** is essentially a line of points (also called nodes). The first node (or the head) points to the next node which eventually points to the last node (or the tail). In this way in a singly linked list, every point has its own information and the the address for its next neighbor. In a doubly linked list, each point has the information for the node before and after itself as well as its own information. 

**The Traveling Salesman** is a machine learning problem that gives the user a list of nodes and distances between the nodes. In one version of the problem, the person or computer is tasked with finding the shortest distance between points that hits every node only once. In another version of the problem, the points must be visited in a closed loop in which every point has a node before and after itself.

While the traveling salesman problem has only been fully solved for every possible case of 22 entered points, it is very interesting to watch the problem being solved in different ways than running hundreds of calculations. Instead, the problem is currently being solved with algorithms, or ways to break down the problem without needing to calculate for every route. At this time one of the algorithms for the looped version of the traveling salesman problem can be solved using self organizing maps.

In this case, self organizing maps cluster nearby points and makes a loop between the clusters, and then finds the most efficient way into, out of, and around each of the clusters that allows for the best access to other clusters and other points. It is very satisfying to see these maps resolve themselves both because it almost looks like a loop melds into the points in question, and because it is so much faster than it would take a computer to calculate through every different iteration of points without using these approximations to begin with.

[Click here to check out an example of the Traveling Salesman Problem being solved with a self organizing map!](https://www.reddit.com/r/gifs/comments/uq42bb/solving_the_travelling_salesman_problem_using/)

[Reading Notes Home Page](README.md)