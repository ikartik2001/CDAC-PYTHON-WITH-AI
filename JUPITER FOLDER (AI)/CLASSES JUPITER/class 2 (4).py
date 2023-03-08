z=[]
for i in range(1,100):
    z.append(i)

for i in range(1,100):
    z.append(+1)
print(z)

month ={"january":31,"feburary":28,"march":31,"april":30,"may":31,"june":30,"july":31,"august":30,"september":31,"october":30,"novomber":31,"december":30}
z= str(input(" enter month name "))

if z=="january"or"feburary"or"march"or"april"or"may"or"june"or"july"or"august"or"september"or"october"or"novomber"or"december":
    print(month[z])
else:
    print("enter again")

z = []
for i in range(0, 1000):
    z.append(i)
print(z)

fruits=['apples','oragnes','Bananas']
quantaties=[5,3,4]
prices=[1.50,2.25,0.89]
z=list[fruits[0],quantaties[0]*prices[0],fruits[1],quantaties[1]*prices[1],fruits[2],quantaties[2]*prices[2]]
print(z)