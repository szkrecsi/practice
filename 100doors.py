indexdoor = [] 
for i in range (0,101): 
    indexdoor.append(False) #fill in list (contains 100 elements) with 'False' elements 
            
for x in range (1,101): #x is for 1.,2.,3. step (101. is for 100.door)
    for i in range (0,101,x): 
        if indexdoor [i] == False: 
            indexdoor [i] = True
        else:
            indexdoor [i] = False

opendoor = [] 
for i in range (0,101):
    if indexdoor [i] == True:
        opendoor.append (i) #fill in and make a list from indexes of opened doors
        print (i) #print indexes of opened doors

print ('The following doors are open: ' + str(opendoor))