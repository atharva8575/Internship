# a="45"
# b=int(a)

# print(b)

# c=input("Enter the String")

# print(c)

# print("abc \n cv \" \'")

# age=18

# if age>=18:
#     print("You Can Drive")
# elif age<0:
#     print("You Put invalid")
# else:
#     print("you can not")


# a="sunday"

# match "Monday":
#     case "sunday":
#         print("yo")
#     case "Monday":
#         print("hh")


# for i in range (1,11):
#       print(i)


# i=0;
# while i<10:
#     print(i)
#     i=i+1

# a="Atharva"
# print(a[-6:-2])


# template=" A {} C {} E"
# B="f"
# D="x"
# s1=template.format(B,D)

# print(s1)

# a=1
# b=2

# print(f"A {a} x {b}")

# def avg(a,b,c):
#     sum=(a+b+c)//3
#     print(sum)

# avg(1,2,3)


# square=lambda x,y:x+y
# print(square(2,3))


# def rec(n):
#     if(n==1):
#        return 1
#     x=n*rec(n-1)
#     return x

# y=rec(5)
# print(y)


# def fibo(n):
#     if(n==0 or n==1):
#         return n;
#     x=fibo(n-1)
#     y=fibo(n-2)

#     return x+y

# ans=fibo(5)
# print(ans)


# import math
# print(math.sqrt(144))


# def square(n):
#     """
#     This function calculates
#     the square of a number.

#     Parameter:
#         n (int): Input number

#     Returns:
#         int: Square of n
#     """
#     return n * n

# print(square.__doc__)


# list=[1,2,3,4,5,6,7]
# print(list)

# my_list = [1, 2, 3]

# my_list.append(4)   # [1, 2, 3, 4]
# my_list.insert(1, 99)  # [1, 99, 2, 3, 4]
# my_list.remove(2)   # [1, 99, 3, 4]
# my_list.pop()       # Removes last element -> [1, 99, 3]
# my_list.reverse()   # [3, 99, 1]
# my_list.sort()      # [1, 3, 99]


# squared = [x**2 for x in range(6)]
# print(squared)  # Output: [0, 1, 4, 9, 16]


# table=[5*i for i in range(1,11)]
# print(table)

# list=[1,2,3,4,5]
# for l in list:
#     print(l)

# listt=[1,2,3,4,5,6]
# a=[1,2,3,4,5,6]

# b=list(zip(listt,a))

# print(b)

# d=[x+y for x,y in b]

# print(d)












# Python Dictionary (dict) Explained

# A dictionary is a collection of key-value pairs.

# Keys are unique.
# Values can be anything (int, string, list, another dictionary, etc.).
# Dictionaries are mutable (can be changed).


# student= {
#     "name":"Atharva",
#     "age":22,
#     "city":"Pune",
#     "yes":True
# }

# print(student)
# print(student["name"])
# student["name"]="Gawade"
# print(student)


# print(student.get("name"))
# print(student.get("salary", "Not"))


# student["salary"]=25000
# print(student)

# del student["yes"]
# print(student)

# print(student)
# student.pop("yes")
# print(student)

# for key in student:
#     print(key)

# for values in student.values():
#     print(values)


# for key, value in student.items():
#     print(key, ":", value)

# xyz={
#     101:{"name":"xyz",
#          "age":12
#          },
#     102:{"name":"xyzx",
#          "age":122
#          },
#     103:{"name":"xyz4",
#          "age":124
#          }
# }

# xyz[101]["name"]="apg"


# xyz.pop(103)

# for i in xyz.values():
#     print(i)

# xyz[101].pop("age")

# print(xyz)

# squares = {x: x*x for x in range(1, 10)}

# print(squares)


# # add= lambda x,y:x+y

# # print(add(1,2))

# list=[x*x for x in range(5)]
# print(list)

# dic={x: x*x for x in range(5)}
# print(dic)



# Python Sets

# A set is an unordered collection of unique elements.

# Features of Sets
# No duplicate values allowed.
# Unordered (no indexing).
# Mutable (can add/remove elements).
# Written using {}.

# s={1,2,3,4,5,6,7,7,7}
# s.add(8)
# s.update([9,10,11,12,13])
# s.remove(13)
# s.remove(14) # here 14 is not present then it will keyerror
# s.discard(14) # 14 is not present so it will not give error
# print(s)
# s.pop()  Removes a random element because sets are unordered.
# for x in s:
#     print(x)

# print(5 in s)   to check wheate it present or not

# print(s)

# set={13+x for x in range(1,8)}
# print(set)


# set operation

# Union | it combines unique element from set
# a={1,2,3,4,5,6}
# b={5,6,7,8,9}
# c=a|b
# print(a.union(b))
# print(c)

# intersection & it only return elemnt that present in both set

# a={1,2,3,4,5,6}
# b={5,6,7,8,9}
# c=a&b
# print(a.intersection(b))
# print(c)

# difference in set  -  here it print that element only present in a not in b

# a={1,2,3,4,5,6}
# b={5,6,7,8,9}
# print(a-b)


# Elements present in either set but not both. Systematic difference(^)
# a={1,2,3,4,5,6}
# b={5,6,7,8,9}
# print(a^b)

# set={5*i for i in range(1,11)}
# print(sorted(set))   # by using sorted() we make set as sorted means order


# t = (10, 20, 30, 40)
# print(t)  # printing tuple
# print(t[0])  # accessing in tuple
# print(t[-1])  # negative index accessing in tuple

# tuples are immutable t[0]=100 not possible

# list=[1,2,3,4,5,6]
# print(list.count(1))

# convert list to tuple

# a=[1,2,3,4,5,5,6]
# t=tuple(a)
# print(t)

# t=(1,2,3,4,5,6,7)
# a=list(t)
# print(a)