list1=["apple", "cherry" ,"banana"]
list2=[1,2,3,4,5,6]
list3=[True,False,False]
print(list3)

mylist = ["apple", "banana", "cherry",6]
print(type(mylist))
#Index number
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#Negative Index 
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry"]
if "apple" not in thislist:
    print("yes")
else:
    print("no")
#use in append()
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

hablolist={1,2,3,4,5}
b=bytes(hablolist)
#b[1]=100    [bytes does not support item assignment]{immutabale}
print(type(b))

hablolist1={1,2,3,4,5}
b1=bytearray(hablolist1)
b1[1]=100 # [bytesarry support item assignment]{mutabale}
print(type(b1))


