steps = input("> ")
lst = steps.split(" ")

count = 0
for i in range(len(lst)):
    if lst[i] == "UP":
        count += int(lst[i+1])
    elif lst[i] == "DOWN":
        count -= int(lst[i+1])
    else:
        pass

print(f"Number of steps from start: {count}")