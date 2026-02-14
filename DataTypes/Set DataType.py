#Create set object
st={"pranav",101,44.22,'A+',101,101}
print(st)  #print only unique values.

#to get the size of set object
print(len(st))   #4-> it will show only unique values in the list.

print("Add single data/element into the set by add() function/method")

st.add(100)
print(st)

print("Add Multiple data/elements into the set by update() function/method")

st.update(["abc","xyz",17])
print(st)

print("Print each element in the set")

for i in st:
    print(i)


print("remove data from the set")
#remove()
st.remove("abc")  #gives and error when element is not available in the set
print(st)

#discard()
st.discard("xyz")   #It will not through any error when element is not available in the set
print(st)

#pop()     #it will remove any random element from the list
st.pop()
print(st)

print("Clear from set")
st1={"pranav",3,2.3,'A+'}
st1.clear()
print(len(st1))

#print("delete overall set")
#del st1
#print(st1)

print("Sorting element in the set work with homogenous data ASC")
st2={100,500,300,200,400}
st2=sorted(st2) # it will sort and return into the list object.
print(type(st2))
print(st2)
print("Sorting element in the set work with homogenous data DSC")
st2.reverse()
print(st2)

print("Converting set object to list object")
st3={"pranav",44,22.22,'A+'}
print(st3)
ls=list(st3)
print(ls)