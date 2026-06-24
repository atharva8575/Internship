# OOPs stand for object oriented programming
# Code reusability
# Better organization
# Easy maintenance
# Real-world modeling

# A class is a blueprint or template for creating objects.

# Think of a class as a design for a car. The actual cars made from that design are objects.

# class car:

#     def speed(self):
#         print("Running...")

# c=car()
# c.speed()


# Constructor in Python
# A constructor is a special method that is called automatically when an object is created.


# class car:

#     name=""  # class  variable
#     top_speed=0   # class  variable
#     def __init__(self,name,top_speed):
#         self.name=name   # instance variable
#         self.top_speed=top_speed  # instance variable
    
#     def info(self):
#         print(self.name)
#         print(self.top_speed)

# c=car("BMW",18)
# # print(c.name)
# # print(c.top_speed)
# c.info()

# class truck:
#     wheels=0

# t=truck()
# t.wheels=4;
# print(t.wheels10)


# class method belong to class variale and instance method belong instance variable

# class car:

#     brand_name=""
#     @classmethod
#     def name(cls,brand_name):
#         cls.brand_name=brand_name
#         print(brand_name)
    
    
#     def top_speed(self,speed):
#         self.top_speed=speed
#         print(self.top_speed)

#     @staticmethod
#     def add(a,b):
#         print(a+b)

    

# car.name("xyz") # way of calling class method
# c=car()
# c.top_speed(120) # way of calling instance method
# car.add(1,2) # way of calling static method


# Inheritance 
# Inheritance is a feature where one class acquires the properties and methods of another class.

# class animal:
#     def eat(self):
#         print("Eating")
#     def sound(self):
#         print("Roar")
    
# class dog(animal):
#     def sleep(self):
#         print("Sleeping now")
    
#     def eat(self):
#         print("Eating food")

# d=dog()
# d.eat()
# d.sound()
# a=animal()


# multiple inheritance 

# class A:
#     def A(self):
#         print("A")
#     def AA(self):
#         print("xyz")
        

# class B:
#     def B(self):
#         print("B")
#     def AA(self):
#         print("xyyz")

# class c(B,A): # MRO(Method Resolution Order) same method when inherited then how they order in which inherited same order get called
#     def A(self):
#         print("AA")
    

# c=c()
# c.A()
# c.AA()

# Polymorphism one method behave different in different from

# class Animal:
      
#       def sound(self):
#             print("Roar")
    
# class dog(Animal):
      
#       def sound(self):
#             print("bark")

# a=Animal()
# a.sound()
# d=dog()
# d.sound()

# Polymorphism with a Loop

# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# class Cow:
#     def sound(self):
#         print("Moo")

# animals = [Dog(), Cat(), Cow()]

# for animal in animals:
#     animal.sound()


# encapsulation Wrapping data (variables) and methods (functions) into a single unit (class) and restricting direct access to data.

# In Python, we make a variable private using __ (double underscore).

# class accounts:
#     def setbalance(self,ammount):
#         self.__ammount=ammount
#     def show_balance(self):
#         print(self.__ammount)

# a=accounts()
# a.setbalance(500)
# a.show_balance()





# Abstraction means:

# Hiding implementation details and showing only the essential features to the user.

# The user knows what to do, but not how it is done internally.

# from abc import ABC, abstractmethod

# class animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class dog(animal):
#     def sleep(self):
#         print("Sleeping")
#     def sound(self):
#         print("Bark")

    
# d=dog()
# d.sleep()
# d.sound()








# Dunder Methods in Python

# Dunder means Double UnderScore.
# These are special methods whose names start and end with double underscores:

# __init__
# __str__
# __len__
# __add__

# They are also called Magic Methods or Special Methods.

#__str__

# class student:

#     def __init__(self,name):
#         self.name=name
    
#     def __str__(self):
#         return f"name is {self.name}"

# s=student("Atharv")
# print(s)


#__len__()

# class team:

#     def __init__(self,l):
#         self.l=l
    
#     def __len__(self):
#         return len(self.l)
    
# l=[5*i for i in range(1,21)]
# t=team(l)

# print(len(t))


# add

# class Number:

#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value

# n1 = Number(10)
# n2 = Number(20)

# print(n1 + n2)


# __eq__()

# class checkin:
    
#     def __init__(self,num):
#         self.num=num
#     def __eq__(self,other):
#         return self.num==other.num
    
# n=checkin(1)
# m=checkin(2)

# print(n==m)

# __lt__

# class num:
#     def __init__(self,num):
#         self.num=num
#     def __lt__(self,other):
#         return self.num<other.num
    
# n=num(1)
# m=num(2)

# print(n<m)






# Error Handling in Python
# Error Handling is used to handle runtime errors gracefully so that the program does not crash.

# try:
#     f=open("a.txt",'r')
#     print(f.read())
#     f.close()
# except Exception as e:
#     print(e)
# finally:
#     print("Not error")  # it always get executd



# try:
#     a=180
#     b=27
#     c=a/b
#     print(c)
# except Exception as e:
#     print(e)
# else:
#     print("Error") # it only execute when no error ocure



