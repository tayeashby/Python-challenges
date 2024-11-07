nums = input("> ")
n = nums.split(" ")
odd_sum = [int(i) for i in n if int(i) % 2 != 0]
print(sum(odd_sum))