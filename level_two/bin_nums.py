""" return binary numbers divisble by 5 """

b = input("Enter binary nums: ")
l = b.split(" ")
nums = []

for num in l:
    length = (len(num)-1)
    total=0
    for j in range(0, length+1):
        s = int(num[j]) * (2**length)
        length-=1
        total+=s

    print(total)

    if total % 5 == 0:
        nums.append(num)

print(nums)

