s = input("Enter a series of words: ")
l = s.split(' ')
n = []
for i in l:
    if n:
        if i not in n:
            n.append(i)
        else:
            continue
    else:
        n.append(i)

for i in range(len(n)):
    for j in range(0, len(n)-i-1):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]

print(n)