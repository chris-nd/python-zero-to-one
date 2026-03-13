def multiple_table(n):
    for table in range(1, n + 1):
        for m in range(1, 13):
            print(f"{table} * {m} = {table*m}")
        print()

multiple_table(5)