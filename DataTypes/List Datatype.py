#ObjectName=[] ---> Syntax of list object creation
#to get the end index of list by --> length-1

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

#Add icnew data at specif position-> right shift operation
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
print("----Remove data element from list")
ls.pop()
print(ls)

#remove element/data from specific index in list-> left shift operation

ls.pop(5)
print(ls)

#remove specific element from list

ls.remove("uttarwar")
print(ls)