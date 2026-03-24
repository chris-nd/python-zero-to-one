def change_variable(a = 0, b = 0):
    a, b = b, a
    return a, b

change_variable(a = 5, b = 10)