def dfs(matrix, label: int):
    for i in range(len(matrix)):
        print(matrix[i])

    visited = set()
    result = []

    def _dfs(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        for neighbor, connected in enumerate(matrix[node]):
            if connected and neighbor not in visited:
                _dfs(neighbor)

    _dfs(label)
    print(result)
    return result


dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1)  # 0 - 1 - 2 - 3
