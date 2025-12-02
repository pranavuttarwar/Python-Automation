#ObjectName=[] ---> Syntax of list object creation
#to get the end index of list by --> length-1

# IMP function:
# append()-> Single data in the end
# extend()-> add multiple data in the list at end
# insert()-> add data in specific index in the list
# pop()-> remove the last data if we add value then remove index data
# Remove()-> remove specific data from the list
# copy()-> it copy the list to another list
# reverse()-> used to reverse the list data
# sort()-> it used to sort data in asc and des for homogenous data
#count(-> occurance of data in the list.
#clear()-> used to remove all element/data from the list

ls=["Pranav",28,"A+",75.5,"Pranav"]

#print type of object
print(type(ls))

#print date of the object
print(ls)

#print size/length of list
print(len(ls))

#print/access single data in the list
print(ls[0])

#add data in the list(extend/append/insert)
#add single data in the last position

ls.append("Nikit")
print(ls)

#Add new data at specif position-> right shift operation
ls.insert(1,"uttarwar")
print(ls)

#Add multiple data in the list
ls.extend(["Papa",100,90.99])
print(ls)

#Replace the existing data in the list
ls[0]="PRANAV"
print(ls)

#Remove data from list(pop()/pop(index)/remove(element))
#remove last element/data from list
print("----Remove data element from list----")
ls.pop()
print(ls)

#remove element/data from specific index in list-> left shift operation

ls.pop(5)
print(ls)

print("----remove specific element from list----")

ls.remove("uttarwar")
print(ls)

print("---Copy list data to another list---")

ls1=ls.copy()
print(ls1)

print("--Get each data in the list---")
for i in ls:
    print(i)

print ("Second Way")

for i in range(0,len(ls)):
    print(ls[i])

for i in range(0,2):
    print(ls[i])

for i in range(7,0):
    print(ls[i])

print("print list data in reverse order")
print(ls)
ls.reverse()
print(ls)

print("print list data in reverse order second way")
for i in range(len(ls)-1,-1,-1):
    print(ls[i])


#Sorting list data by ascending and descending
print("LIst can be sort with homogenous data")

p=[90,60,99,43,12,12,0,44,12,0]

print("Before sorting")
print(p)
p.sort()   #it will sort in ascending
print("After sorting")
print(p)

print("Reverse order the list")
p.reverse()
print(p)

print("Show the occurrence of data in the list")

print(p.count(12))