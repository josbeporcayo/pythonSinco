#Loops

forloops=[0,1,2,3,4,5,6,7,8]

for f in forloops:
    pass

    #print(f+2)

Listoflist=[[0,1,2],[3,4,5],[6,7,8]]

## 0 1 2
## 3 4 5
## 6 7 8

for l in Listoflist:
    y=0
    print(l)

    for u in l:
        print(u)
        y+=u # igual a y=y+u
    
    print(y)

#continue #pass #break

forloops=[1,2,3,4,5,6,7,8,9,10]

suma=0

for elem in forloops:
    

    if (elem % 2)==0:
        suma+=elem
    else:
        continue

#print(suma)

forloops=[1,2,3,4,5,6,7,8,9,10]

suma=0

for elem in forloops:
    

    if (elem % 2)==0:
        suma+=elem
    elif elem<=8:
        continue
    else:
        break

print(suma)


ingreso=input('Escribe y para sí y n para no ')

while ingreso=='y':
    print('Síiiiiiiiiiiiiiiiiiiiiiiii')
    ingreso=input('Escribe y para sí y n para no ')

i=0
while i<6:
    if i==3:
        break
    print(i)
    i+=1








        

    

