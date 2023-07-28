list1= [2,3,"Hello",4.0, [44,55,66]]
size= len(list1)
#print(list1)

#fetching single ele
#print(list1[4][2])  #to fetch the inner/nested list elements

#slicing the list
#print(list1[0::+1]) #with slice operator

#reverse slicing
#print(list1[-1::-1])    #to reverse the string

#print every ele one by one
# for n in range(0,size,+1):      #main advantage of range() here is we can iterate in both forward and backward direction
#     print(list1[n])

list2= [10,20,30,40]
#print every ele one by one [Another way]-- it is not iterate in backward direction !
for n in list2:
    print(list2)
    
#print in reverse order
for  i in range(size-1,-1,-1):
    print(list1[i])