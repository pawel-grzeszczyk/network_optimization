def incidence_to_adjacency(incidence_matrix):
    # vertices_no
    vertices_no = len(incidence_matrix)
    # edges_no
    edges_no = len(incidence_matrix[0])

    adjacency_matrix = [[0]*vertices_no for i in range(vertices_no)]

    # iterating over edges_no
    for column in range(edges_no):

        # placeholders for start and end of a vertex
        start, end = None, None

        # iterating over vertices_no
        for row in range(vertices_no):

            # looking for the edge, where vertex leaves:
            if incidence_matrix[row][column] == 1:
                start = row

            # looking for the edge, where vertex enters:
            if incidence_matrix[row][column] == -1:
                end = row

        adjacency_matrix[start][end] = 1
        adjacency_matrix[end][start] = 1

    return adjacency_matrix


def user_input():
    while True:
        incidence_matrix_str = input(
            'Enter incidency matrix as a list of lists:')
        try:
            incidence_matrix = eval(incidence_matrix_str)
            return incidence_matrix
        except:
            print('This is not a list of lists')


print('\nThis program transforms the incidence matrix of a given diagraph into its adjacency matrix.\n')

while True:
    incidence_matrix = user_input()

    for row in incidence_matrix:
        print(row)

    is_correct = input("Is this correct? (Yes/No) ").lower()

    if is_correct == 'yes':
        adjacency_matrix = incidence_to_adjacency(incidence_matrix)
        print('\nAdjacency matrix:')
        for row in adjacency_matrix:
            print(row)
        break

    elif is_correct == 'no':
        print("Please enter the incidency matrix again.\n")
        continue

    else:
        print("Invalid input. Please enter the incidency matrix again.\n")


if __name__ == "__main__":
    input('\nPress Enter to exit')
# [[1, 1, 0, 0, 0], [-1, 0, -1, 0, 0],[0, -1, 1, 1, -1], [0, 0, 0, -1, 1]]
