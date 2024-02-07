#Single  Inheritance
class Parent():
    def Output(self):
        print("this if parent calss")
class Child(Parent):
    def OutputChild(self):
        print("this is child class")
i=Child()
i.OutputChild()
i.Output()

#Multiple Inheritance
class Father():
    def Output(self):
        print("this is father class")
class Mother():
    def OutputM(self):
        print("this is mother class")
class Child(Father,Mother):
    def OutputChild(self):
        print("this is child class")
ice=Child()
ice.Output()
ice.OutputChild()
ice.OutputM()

#Multilevel Inheritance
class GrandFather():
    def Output(self):
        print("this is gf class")
class Father(GrandFather):
    def Outputf(self):
        print("this is father class")
class Child(Father):
    def OutputChild(self):
        print("this is child class")
ice=Child()
ice.Output()
ice.Outputf()
ice.OutputChild()
    
#Hierarchial Inheritance
class Father():
    def Output(self):
        print("this is father class")
class Child1(Father):
    def OutputChild1(selF):
        print("this is child1 class")
class Child2(Father):
    def OutputChild2(self):
        print("this is child2 class")
ice=Child1()
cream=Child2()
ice.Output()
cream.Output()
ice.OutputChild1()
cream.OutputChild2()

# class MethodOverload():
#     def Something(self,a,b,c):
#         print(a,b,c)
# obj=MethodOverload()
# obj.Something(1,2,3)
# obj.Something(1,2)
# obj.Something(1)
# obj.Something()

class MethodOverload():
    def Something(self,a=None,b=None,c=None):
        print(a,b,c)
obj=MethodOverload()
obj.Something(1,2,3)
obj.Something(1,2)
obj.Something(1)
obj.Something()

class MethodOverriding():
    def Display(self):
        print("this is parent class")
class Child(MethodOverriding):
    def Display(self):
        print("This is child class")
obj=Child()
obj.Display()

class MethodOverriding():
    def Display(self):
        print("this is parent class")
class Child(MethodOverriding):
    def Display(self):
        print("This is child class")
        super().Display()
obj=Child()
obj.Display()


class GrandFather():
    def __init__(self,a):
        self._y=a
        print(self._y)
class Father(GrandFather):
    def Display1(self):
        print(self._y)
class Child2(Father):
    def Display2(self):
        print("child2",self._y)
obj=Child2(15)
obj.Display1()
obj.Display2()


# class GrandFather():
#     def __init__(self,a):
#         self.__y=a
#         print(self.__y)
# class Father(GrandFather):
#     def Display1(self):
#         print(self.__y)
# class Child2(Father):
#     def Display2(self):
#         print("child2",self.__y)
# obj=Child2(15)
# obj.Display1()
# obj.Display2()

#glaobal and local Variables

a=10
def func():
    b=20
    print("this is func",b,a)
func()
print(a)
print(b)

#Abstraction

from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")
class Suziki(Car):
    def mileage(self):
        print("The mileage is 25kmph")
class Duster(Car):
    def mileage(self):
        print("The mileage is 20kmph")
class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph")
t=Tesla()
t.mileage()
r=Renault()
r.mileage()
s=Suziki()
s.mileage()
d=Duster()
d.mileage()
# c=Car()
# c.mileage()


        







    
    

    

    


