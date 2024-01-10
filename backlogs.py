#DICTIONARY COMPREHENSION
dict = {x:x**2 for x in [1,2,3,4,5]}
print(dict)

demodict = {x.upper():x*2 for x in 'cubexo'}
print(demodict)

demo = {x:x**2 for x in range(10) if x*5 % 2 == 0}
print(demo)

demoo = {x:x*10 for x in range(25) if x**2 % 5 == 0}
print(demoo)

stringdemo = "riseandshine"
dictt = {
    x:{y:x+y for y in stringdemo} for x in stringdemo 
}
print(dictt)

#TUPLE COMPREHENSION
tupp = (1,2,3,4,5)
print("the old tuple is:")
print(tupp)
newtupp = tuple((x**2 for x in tupp)) # we have obtained a tuple using generator comprehension and the tuple() function.
print("new tuple is:")
print(newtupp)

tupp = (1,2,3,4,5)
print("the old tuple is:")
print(tupp)
newtupp = *(x**2 for x in tupp), #You need to unpack the generator created from generator comprehension using the * operator. 
                                 #Then, you can place a comma “,” at the end of the unpacked elements to create a tuple
print("new tuple is:")
print(newtupp)

tupp = (1,2,3,4,5)
print("the old tuple is:")
print(tupp)
newtupp = tuple([x**2 for x in tupp]) #List comprehension and the tuple() function to imitate tuple comprehension 
print("new tuple is:")
print(newtupp)

upp = (1,2,3,4,5)
print("the old tuple is:")
print(tupp)
newtupp = *[x**2 for x in tupp], #unpacking operator with list comprehension to imitate tuple comprehension 
print("new tuple is:")
print(newtupp)

#ENUMERATE
l1 = ['rise', 'and', 'shine']
obj1 = enumerate(l1)
print(type(obj1))
print(list(enumerate(l1)))

S1 = "riseandshine"
obj2 = enumerate(S1)
print(type(obj2))
print(list(enumerate(S1)))

l1 = ['rise', 'and', 'shine']
for x in enumerate(l1):
    print (x)

for count, ele in enumerate(l1,200):
    print(count,ele)

for count,ele in enumerate(l1):
    print(count)
    print (ele)

#DESTRUCTURING
my_dict = {"name": "krati" , "age": 22}
x,y = my_dict
print(x)
print(y)

x,y = my_dict.values()
print(x)
print(y)