#Variable types
x=1 #int
y=1.56 #float
z='Jose Luis Porcayo' #str
a=True #bool

print(type(x))
print(type(y))
print(type(z))
print(type(a))

#Data types

#####################list and list methods
lista=[8,7,9,10,'José Luis']
#lista=list(8,7,9,10,'José Luis') alternative method for lists
print(type(lista))
print(lista)

print(lista[0])
print(lista[0:3]) #get list elements from 0 up to but not including 3
print(lista[-1])

lista.append(100) #Append an element to my list

print(lista)

lista.pop(4) #eliminate list element

print(lista)

lista.sort() #sort list gives error when different data types are present

print(lista)

print(len(lista)) # length of list

####################Dictionaries

diccio={'llave':'valor','llave2':[0,1,2,3,4,5],'llave3':9.0}

print(diccio)

print(diccio['llave'])

print(diccio['llave2'])

print(diccio['llave2'][0:3])

########################Tuples

x,y,z=(1,2,3)

print(x)
print(y)
print(z)

u=(1,2,3)

print(u,type(u))

print(u[0])

#Conditionals

variable=9

variable2=8

variable3=10

# > < >= <= ==  ' is in '
if variable>5:
    print("Sí es mayor a 5")
elif variable>10:
    print('Sí es mayor a 10')
else:
    print('No sé que pasó')

# and or not

if variable>5 and variable2>5: # if (variable1 and variable2)>5:
    print("Ambas son mayor a 5")
elif variable>10:
    print('Sí es mayor a 10')
else:
    print('No sé que pasó')

if variable>5:
    if variable2>5:
        print('Ambas son mayor a 5')
else:
    print('No son mayor a 5 las 2')









