def hanoi_solver(n: int):
    rods = [list(range(n, 0, -1)), [], []]
    hist = []

    def snapshot():
        hist.append(" ".join(str(r) for r in rods))

    def move(num, src, tgt, aux):
        if num == 1:
            rods[tgt].append(rods[src].pop())
            snapshot()
            return
        move(num - 1, src, aux, tgt)
        rods[tgt].append(rods[src].pop())
        snapshot()
        move(num - 1, aux, tgt, src)

    snapshot()
    move(n, 0, 2, 1)

    return "\n".join(hist)


print(hanoi_solver(3))
