def fibonacci(n: int):
    if n < 2:
        return n

    sequence = [0, 1]
    sequence.extend([0] * (n - 1))

    for i in range(2, n + 1):
        sequence[i] = sequence[i - 1] + sequence[i - 2]

    return sequence[n]


fibonacci(10)
