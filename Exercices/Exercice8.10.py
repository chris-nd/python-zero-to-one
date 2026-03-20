def pascal_triangle(n):
    lp = [1]
    for _ in range(n):
        nl = lp + [1]
        for i in range(len(lp) - 1):
            nl[i + 1] = lp[i] + lp[i + 1]
        lp = nl
        print(nl)

pascal_triangle(1)
            