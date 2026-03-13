def adjacency_list_to_matrix(alist: dict):
    n = len(alist)
    matrix = [[0] * n for _ in range(n)]
    for i, nodes in alist.items():
        for j in nodes:
            matrix[i][j] = 1
        print(matrix[i])
    return matrix


adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})
