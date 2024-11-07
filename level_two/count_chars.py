s=input("> ")
k = s.split(' ')
m = (''.join(k))
nums=0
chars=0
for i in m:
    if i.isdigit():
        nums +=1
    else:
        chars +=1

print(f"Nums: {nums}, Chars: {chars}")