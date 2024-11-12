tup = ( 1,2,3,4,5,6,7,8,9,10 )
n = str(tup).split(",")

for i in range(len(n)):
    if i == 4:
        print(n[0:i])
    elif i == 9:
        print(n[5:i])
    else:
        pass
