num = input("Enter num > ")
cal = "a+aa+aaa+aaaa"

new = cal.replace("a", num)
n = new.split("+")

total=0
for i in n:
    sum = int(num) ** len(i)
    total += sum

print(total)

