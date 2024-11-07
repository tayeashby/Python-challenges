
s = input("Enter a series of words: ")
n = s.split(", ")
ol=[]

alphabet="abcdefghijklmnopqrstuvwxyz"

first_letters=[]
for i in n:
    first_letters.append(i[0])

for i in alphabet:
    if i in first_letters:
        for j in n:
            if j[0] == i:
                ol.append(j)

f = ", ".join(ol)
print(f)


