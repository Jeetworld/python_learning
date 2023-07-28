s= "Welcome to Programming World !!"
size=len(s)
print("length of string s is ", size)

# #One Way - forward
# for i in range(0, size, 1):
#     print(s[i])
#
# #second way
# slice=s[0:size:1]
# print(slice)

#reverse loop
# for t in range(size-1, 0, -1):
#     print(s[t])


#Another Way to iterator the string
for k in s:
    print(k)