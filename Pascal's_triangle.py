def triangles():
    L = [1]
    while True:
        yield L
        L = [L[0] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [L[-1]]]
