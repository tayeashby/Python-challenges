num = int(input("Enter a number: "))
for i in range(num-1, 0, -1):
    num *= i

print(num)