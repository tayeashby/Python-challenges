class NumGenerator:
    def __init__(self, nums):
        self.nums = nums

    def generate_nums(self):
        for i in range(self.nums+1):
            if i % 7 == 0:
                yield i

obj = NumGenerator(50)

for num in obj.generate_nums():
    print(num)