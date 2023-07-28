def simpleFunction():
    print("***this is my simple function***")
    print("***this is my first function !!***")

def argumentFunction(a,b):
    print(a+b)

def returnFunction(x,y=2):
    print(x+y)
    c = x + y
    return c

simpleFunction()    #to call simple function
argumentFunction(10,20)         #to call argumented function
output = returnFunction(10)
print("value of retun function is ", output)