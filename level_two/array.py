def array(x, y):
    list = []
    for i in range(x):
        sub_list=[]
        list.append(sub_list)
        for j in range(y):
            sub_list.append(i*j)

    return list

n1 = int(input("> "))
n2 = int(input("> "))
print(array(n1, n2))