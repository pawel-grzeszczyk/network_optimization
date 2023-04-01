## User Guide for Incidence to Adjacency Matrix Converter

This program takes an incidence matrix of a directed graph as input and outputs the corresponding adjacency matrix.

### Requirements

- This program requires Python 3.

### Usage

1. Run the program.
2. Enter the incidence matrix as a list of lists when prompted.
3. Check if the displayed matrix is correct.
4. If the matrix is correct, type "yes" and hit enter.
5. If the matrix is not correct, type "no" and hit enter, then repeat step 2.
6. The program will then display the resulting adjacency matrix.

### Input Format

The incidence matrix should be entered as a list of lists, with the vertices as rows and the edges as columns. The matrix should contain the following values:

- 1 if the edge leaves the vertex
- -1 if the edge enters the vertex
- 0 if the edge is not connected to the vertex

Example input:
[[1, 0, 0, 0, -1],
 [0, 1, -1, 0, 0],
 [0, -1, 1, -1, 0],
 [0, 0, 0, 1, 1]]

### Output Format

The program will output the corresponding adjacency matrix as a list of lists. The matrix will contain the following values:

- 1 if there is an edge connecting the vertices
- 0 if there is no edge connecting the vertices

Example output:
[[0, 1, 0, 0],
 [1, 0, 1, 1],
 [0, 1, 0, 1],
 [0, 1, 1, 0]]

### Exit the program

Once the algorithm is executed, the program will wait for you to press Enter to exit.
