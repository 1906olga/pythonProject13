def square (side):
    P = 4 * side
    S = side ** 2
    D = side * (2 ** (0.5))
    return [P, S, D]
print (square(16))
