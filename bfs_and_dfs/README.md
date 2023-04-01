## DFS and BFS Algorithm Implementation

This Python program implements the Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms to traverse a graph represented as an adjacency list.

### Requirements

- This program requires Python 3.

### Usage

1. Run the program.
2. Enter the graph in the form of an adjacency list.
3. The program will display the adjacency list entered.
4. Confirm if the displayed adjacency list is correct. If not, re-enter the graph.
5. Enter the starting vertex.
6. Enter the algorithm you want to use (DFS/BFS).
7. The program will display the order in which the vertices are visited by the algorithm.

### Input Format

The graph should be entered as a dictionary where vertices are keys and their values are neighbors of a particular vertex.
Example:
{
'0': ['1'],
'1': ['0', '2', '5'],
'2': ['1', '3', '4'],
'3': ['2'],
'4': ['2'],
'5': ['1', '6'],
'6': ['5', '7'],
'7': ['6']
}

### Output Format

The program will output the vertices in the order they are visited by the chosen algorithm.

### Exit the program

Once the algorithm is executed, the program will wait for you to press Enter to exit.

### Possible Errors

- If the input graph is not in the correct format, an error message will be displayed asking to enter the graph again.
- If the starting vertex is not in the graph, an error message will be displayed.
- If an algorithm other than DFS or BFS is entered, an error message will be displayed.
