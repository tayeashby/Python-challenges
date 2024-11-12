#whole dict
def sq_dict(nums):
    dict={}
    for i in range(nums):
        dict[i] = i**2
    
    return dict

print(sq_dict(21))

#Values only
def sq_dict2(nums):
    dict={}
    for i in range(nums):
        dict[i] = i**2
    
    return dict.values()

print(sq_dict2(21))

#Keys only
def sq_dict3(nums):
    dict={}
    for i in range(nums):
        dict[i] = i**2
    
    return dict.keys()

print(sq_dict3(21))



