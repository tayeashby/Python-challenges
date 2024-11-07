from math import sqrt

def q(d, c=50, h=30):
    return sqrt((2*c*d)/ h)

nums = input("Enter numbers: ")
n = nums.split(',')
print(n)
for i in n:
    print(f"{q(int(i)):.0f}")