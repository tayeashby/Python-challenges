class String:
    def __init__(self):
        self.string = None

    def get_string(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string)

str1 = String()
str1.get_string()
str1.printString()