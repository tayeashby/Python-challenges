s = input("> ")
lower=0
upper=0
for i in s:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    else:
        pass

print(f"Upper: {upper}, Lower: {lower}")

