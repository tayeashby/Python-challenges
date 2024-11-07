""" Check for every digit being even """


for i in range(1000, 3000):
    even_count = 0
    for j in str(i):
        if int(j) == 0:
            break
        else:
            if int(j) % 2 == 0:
                even_count += 1

    if even_count == len(str(i)):
        print(i)
    
            

    
        
                

        
 