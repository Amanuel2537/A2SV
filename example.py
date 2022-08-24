def myDecorator(function):
    def wraper():
        print("I am decorating the Function")
    return wraper
def helloworld():
    print("hello world")
myDecorator(helloworld())






'''
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x + other.x,self.y+other.y)
    def __repr__(self):
        return f"X:{self.x},Y:{self.y}"
 
v1=Vector(20,39)
v2=Vector(1,24)
v3=v1+v2
print(v3.x)
print(v3.y)    
print(v3.x,v3.y)    
print(v3)

def solve(nums):
    count=0
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            count+=1
    return count
nums=[1,1,1,1]
print(solve(nums))
   '''     
        