def dfs_n_queens(n: int):
    if n < 1:
        return []

    solutions = []

    def is_safe(placement, row, col):
        for r in range(row):
            c = placement[r]
            if c == col:
                return False
            if abs(row - r) == abs(col - c):
                return False
        return True

    def dfs(row, placement):
        if row == n:
            solutions.append(placement[:])
            return
        for col in range(n):
            if is_safe(placement, row, col):
                placement.append(col)
                dfs(row + 1, placement)
                placement.pop()

    dfs(0, [])
    return solutions


print(dfs_n_queens(4))
