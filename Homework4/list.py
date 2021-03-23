#List

myUniqueList=[]
leftOver=[]

def isThere(data):
    if data in myUniqueList:
        rejected(data)
        return True
    else:
        myUniqueList.append(data)
        print("myUniqueList ",myUniqueList)
        return False

def rejected(value):
    leftOver.append(value)
    print("leftOver",leftOver)

myUniqueList.append(1)
two=isThere(2)
print(two)
three=isThere(3)
print(three)
againTwo=isThere(2)
print(againTwo)
