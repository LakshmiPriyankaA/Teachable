# Teachable

# The flavour of SQL that I chose to represent the NeighboringNode class is the plain SQL.

# I have written 3 methods 
  1. init(constructor): When ever we instantiate the object for the class NeighboringNodes with size and debug, it will construct a grid of size x size nodes. For        example, if size = 3, NeighboringNodes will instantiate a 3x3 grid. If the debug is true, the method will print the (x, y, i) features for each of the nodes        after the grid is built. 
  2. index_node: This method accepts index as user input and returns the (x,y) coordinate of that node.
  3. topological_nodes: This method accepts either x & y OR i and using the supplied parameters it returns coordinates of all the neighboring nodes, based on the        provided topological neighborhood type, within distance m.
  
