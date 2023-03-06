#class 3, CDAC
import distutils.sysconfig
from typing import Dict

# dictionary

d = dict()
info = {'name':'kartik',"age":21,"eligible":True}
print(info["name"])
print(info.get("age"))

# printing different value so get the specific items out of dictionary
print(info.values())
print(info.keys())
print(info.items())

#adding dob to dictionary

info.update({"DOB":2001})
print(info)
print(info["DOB"])

# deleting age from info.
del info['age']
print(info)

new_dictionary = info.copy()
print(new_dictionary)

# DICTIONARY ACCETPS TWO SAME VALUES
d1 = {"1":234,"1":2}
print(d1)

print(d1["1"])


# CREATING A TWO ELEMENT DICTIONARY

d2  = {"kartik":{"name":"kartik","age":21,"hometown":"sundarnagar","car":"bughati"},"chaju":{"name":"chaju doodhvala","age":26,
           "car":"maruti800"}}
print(d2["kartik"])
print(d2["chaju"])

################### OPERATIORS

a =20
b= 5
c= a+b
print(c)
d = a*b
e = a/b
print(d)
print(e)

f =  b%a
print(f)


print(345>34)

print("hi" == "bye")

print(1>=1)

x = False
print(x)

# if else statement

dog = "dog can bark"

if 1<2:
                             print("yelp")

if 2>198:
    print("yipi")
else:
    print("sorry buddy , momy's not home ")

kar = "kartik"
shar = "kartik"
i=0


if kar==shar:
     print("both are equal")
     kar = kar+str("thakur")
else:
     print("not are same")


## if and elif

num = 18
if (num<0):
    print("number is negative")
elif (num<=10):
    print("number is between 1-10")
elif(num >10 and num<=20):
    print("number is between 11-20")
else:
    print("number is greater than 20")


 # question given
# write a program to check weather the last digit of number entered by user is divisible by 3 or not

num1= int(input("enter your number boss"))

remainder = 3 % num1
print(remainder)


#write a program to check weatehr a person is eligible for voting or not

age =  int(input("enter your age"))

if age>18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting accourding to art19 of indian constitution")



count = 10000000000000
while(count>0):
    print(count)
    count = count-100000000000^22
i = 1
while (i <= 10):
    i = i + 1
    if (1 % 2 != 0):
        continue
    print(i)
