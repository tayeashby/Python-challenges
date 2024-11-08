i = input("> ")
n = i.split(" ")
final = []

for i in n:
    t = i.split(',')
    tup = (t[0], t[1], t[2])
    final.append(tup)
 

ol =[]
while len(final) > 0:
    highest = 0
    winner = None
    for i in final:
        sum = int(i[1]) + int(i[2])
        if sum > highest:
            highest = sum
            winner = i

    final.remove(winner)
    ol.append(winner)

print(ol)