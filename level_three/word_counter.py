words = input("> ")
n = words.split(" ")
count = {}
for i in n:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)
 