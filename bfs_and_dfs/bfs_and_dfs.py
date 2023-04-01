def dfs_and_bfs(graph, start, algorithm):
    if algorithm == 'DFS':
        print('\nDFS algorithm:')
        ix_to_pop = -1
    elif algorithm == 'BFS':
        print('\nBFS algorithm:')
        ix_to_pop = 0
    else:
        return 'There is no such algorithm. Select DFS or BFS.'
    # Set of visited nodes
    visited = set()
    # Stack to store nodes to visit (neighbors of previously visited node)
    stack = [start]

    while stack:
        # Take next element of the stack
        # Last element if DFS
        # First element if BFS
        node = stack.pop(ix_to_pop)

        # if the node from the stack was not yet visited go there
        # else move on to the next element in the stack
        if node not in visited:
            visited.add(node)
            print(node)  # Print the visited node

            # Loop over the neighbors of currently visited node
            # and add them to the stack if they were not yet visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


def user_input():
    while True:
        adj_list_str = input(
            'Enter a graph represented as an adjacency list. \n(A dictionary where vertices are keys and and values are neighbors of a particular vertex.)\n')
        try:
            adj_list = eval(adj_list_str)
            dict(adj_list)
            return adj_list
        except:
            print(
                "\nWrong formatting. Try again. Here is an example: {'0': ['1', '2'], '1': ['0'], '2': ['0']}\n")


while True:
    graph = user_input()

    print('')
    for k, v in graph.items():
        print(f'{k}: {v}')

    is_correct = input("Is this correct? (Yes/No) ").lower()

    if is_correct == 'yes':
        start_point = input('Which vertice do you want to start from? ')
        if start_point not in graph.keys():
            print('\nStart point should be one of the vertices in the graph.')
            break

        algorithm = input(
            'Which algorithm do you want to use? (DFS/BFS) ').upper()
        if algorithm != 'DFS' and algorithm != 'BFS':
            print('\nWrong algorithm. Select DFS or BFS.')
            break

        adjacency_matrix = dfs_and_bfs(graph, start_point, algorithm)
        break

    elif is_correct == 'no':
        print("Please try again.\n")
        continue

    else:
        print("Invalid input. Please enter the adjacency list again.\n")


if __name__ == "__main__":
    input('\nPress Enter to exit')
# {'0': ['1'], '1': ['0', '2', '5'], '2': ['1', '3', '4'], '3': ['2'], '4': ['2'], '5': ['1', '6'], '6': ['5', '7'], '7': ['6']}
