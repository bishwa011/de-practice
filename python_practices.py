#BASICS
# name = input("What is your name?")
# age = input("What is your age?")
# print (f"Hello {name}, Your are {age} years old")

# num1= int(input("Enter any number"))
# num2 = int(input("Enter any number"))

# add = num1 + num2
# sub = num1 - num2
# mul = num1 * num2
# div = num1 / num2
# rem = num1 % num2

# print (f"Addition = {add}\n")
# print (f"Subtraction = {sub}\n")
# print (f"Multiplication = {mul}\n")
# print (f"Division = {div}\n")
# print (f"Reminder = {rem}\n")


# C = int (input("What is the temperature today in Celsius today?"))
# F = (C * 9/5) +32
# print(f"Thats {F} Farenheit ")

# num = int(input("Enter any number \n"))

# if (num > 0):
#     print (f"{num} is positive")
# elif (num < 0):
#     print (f"{num} is negative")
# else:
#     print(f"{num} is zero")


# year = int(input("Enter the year"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print (f"Year {year} is Leap year")
#         else:
#             print (f"Year {year} is NOT a Leap year")
#     else:
#         print (f"Year {year} is Leap year")
# else:
#     print (f"Year {year} is NOT aLeap year")

# if year % 400 == 0:
#     print (f"Year {year} is Leap year")
# elif year % 100 == 0:
#     print (f"Year {year} is NOT a Leap year")
# elif year % 4 == 0:
#     print (f"Year {year} is Leap year")
# else: 
#     print (f"Year {year} is NOT a Leap year")


# a = int (input("Enter num 1"))
# b = int (input("Enter num 2"))
# c = int (input("Enter num 3"))


# if a > b:
#     if a > c:
#         print(f"{a} is greatest") 
#     else:
#         print(f"{c} is greatest")
# else:
#     if b > c:
#         print(f"{b} is greatest")
#     else:
#         print(f"{c} is greatest")


# num = int(input("Enter maximum number "))
# a=1
# while (a<=num):
#     print (f"{a}\n")
#     a+=1

# for i in range (1,100):
#     print (i)


# odd / even
# for i in range (1,100,2): // (2,100,2)
#     print (i)

#Even/odd numbers print only
# for i in range (1,100): 
#     if i%2==0: #i%2!=0
#         print (i)

# n = int(input("Enter the number"))
# sum = 0

# for i in range (1,n+1):
#     sum=sum+i

# print (f" Sum upto {n} = {sum}")


# n = int(input("Enter the numver\n"))

# for i in range (1, 11):
#     print (f"{n} * {i} = {n*i}\n")


# str = input("Enter a string")
# # print(str[::-1]) // approach 1 (easiest)

# # for i in range (0, len(str)):
# #     print (f"{str[len(str)-i-1]}") //Prints vertically

# rev_str = ""

# for i in range (len(str)-1,-1,-1):
#     rev_str+= str[i]


#COUNT VOWELS

text = input("Enter the text")
count = 0

for char in text:
    if text[i] in 'aeiouAEIOU' :
        count += 1
print(f"Total vowels in {text} = {count}")










































