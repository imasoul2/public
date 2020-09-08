import math as moth
import numpy


class Person:
    def __init__(self,name="no name",age=999):
        self.name = name
        self.age = age
    
    def work(self,minute):
        print("{} just worked for {} minutes".format(self.name, minute))
    
    def eat(self,*kids):
        for x in kids:
            print(x)


class Student(Person):
    
    # method override
    
    def work(self,minute,whom):
        super().work(minute) # calling method from super class
        print("{} just worked for {} minutes with {}".format(self.name, minute, whom))
        
    

p1 = Person("Bob", 22)
p2 = Student("Carl", 25)
p2.work(15,"Caroline")
p2.eat("a","ab","c")

class Math:
    
    @staticmethod
    def add(a,b):
        return a+b

print(Math.add(1,2))

# having multiple args with the keywords
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



# resursive functison
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
