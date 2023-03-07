class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        temp = MathDojo()
        print(temp.result)
        for a in nums:
            result += a
        return result
    def subtract(self, num, *nums):
        result -= num
        for a in nums:
            result -= a
        return self
    
# create an instance
md = MathDojo()
# to test:
x = md.add(2)
print(x)
