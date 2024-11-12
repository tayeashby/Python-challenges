def sq_list(rng):
    sq = []
    for i in range(rng):
        sq.append(i**2)

    return sq[:-6:-1]

print(sq_list(21))