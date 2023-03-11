# CLASS 2 , CDAC PYTHON WITH A , KARTIK THAKUR 28/2/2023

# 1 TUPPLE AND ITS FEATURES

details=("abhijeet",18,"ashish",9.8)  # IT IS A TUPPLE
print(details)

#Print alternatate values in each tupple

animals = ["cat","dog","cat","bat","pig","horse","donkey","goat","COW"]
print(animals [::2])

# CONCATENATE TUPPLES

countries  = ("pakistan","Afganistan","bangladesh","shrilanka")
coutnries2= ("vietnam","india","china")
southeastasia = countries+coutnries2
print(southeastasia)

#unpack tupples  and ASSINGING VALUE TO TUPPLE

info = ("kartik",21,"JNGEC")
(name,age,university)= info
print("name",name)
print("age",age)
print("university",university)

# ASSIGNING VALUE TO TUPPLE ...at random

animalsT = ('cat', 'dog', 'cat', 'bat', 'pig', 'horse', 'donkey', 'goat', 'COW')
(*janwar,bird,fish)= animalsT
print(janwar)
print(bird)
print(fish)

## SETS

s1 ={1,2,3,}
s={1,2,3,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,"KARTIK"}
print(s)

cities = {"pathankot","mohali","shimla","Dharampur"}
cities.add("kullu")

#print(cities)


cities.update({"indore","kangra","haryana"})
print(cities)

#UNION
value = {5,6,1,2,3,7}
value2 ={1,2,3,4,7}


print(value.remove(1))
print(value)

##   .isdisjoint()


##    .issubset(cities)
cities1 = {"shimla","mumbai","kausali","haryana"}
cities_copy ={"mumbai","kausali"}

print(cities_copy.issubset(cities))









