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

# text = input("Enter the text")
# count = 0

# for char in text:
#     if text[i] in 'aeiouAEIOU' :
#         count += 1
# print(f"Total vowels in {text} = {count}")

# text = input("Enter text")
# text= text.split()

# for word in text:
#     print(word)

# text = input("Enter text")
# rev_text = text[::-1]

# if text == rev_text:
#     print(f"{text} is Palindrome")
# else:
#     print(f"{text} is not Palindrome")

# A = [10,20,30,40,50]
# sum = 0
# for i in A:
#     sum+=i
# print(f"Sum = {sum}")
# print("Average =", sum/len(A))

# A = []
# for i in range (0,5):
#     x = int(input("Enter the number"))
#     A.append(x)

# print(A[::-1])


# list_A = [1,2,2,3,4,4,5]
# list_B = []

# for item in list_A:
#     if item not in list_B:
#         list_B.append(item)

# print(list_B)

# original = [10,5,20,8,15]
# largest = original[0]
# slargest = original[1]

# if largest < slargest:
#     largest, slargest = slargest, largest

# for item in original:
#     if item > largest:
#         slargest = largest
#         largest =item
#     elif item > slargest:
#         slargest = item

# print(f"S-largest = {slargest}")

#=================================================================================

# def large (a, b):
#     if a<b:
#         return b
#     elif b<a:
#         return a
#     else:
#         return "Both are equal"
# print(large(10,2))

# def is_prime(a):
#     count = 0
#     if a<2:
#         return False
#     for i in range (2,int(a ** 0.5)+1):
#         if a%i ==0:
#             return False
#     return True

# print(is_prime(21))


# def factorial (a):
#     if a < 0:
#         return "Negativer number is invalid"
#     elif a == 0 :
#         return 1
#     else:
#         return a*factorial(a-1)
    
# print("factorial of 5 is", factorial(5))
# print("factorial of 5 is", factorial(-5))


# def filter_list(original):
#     filtered = []
#     for item in original:
#         if item % 2 == 0:
#             filtered.append(item)
#     return filtered

# main_list = [1,2,3,4,5,6,7,8,9,10]

# print("Filtered list is ", filter_list(main_list))


# try_dict = {"a": 50, "b": 60}
# try_dict["c"] = 40
# total = 0
# for name, values in try_dict.items():
#     print(name, ":", values, "\n")
#     total += values

# print (f"Average grade :{total/len(try_dict)}" )
# highest_std = max(try_dict, key = try_dict.get)
# print("Highest grade= ",highest_std, "with ", try_dict[highest_std] )


input_var = input("Enter text")

input_var = input_var.split()
word_count = {}

for item in input_var:
    if item in word_count:
        word_count[item] +=1
    else:
        word_count[item] = 1

for item, count in word_count.items():
    print(item, ":", count )






























