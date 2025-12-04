dict1={1:"pranav",2:"Nikita",3:"Tejas",4:"Pattewar","Papa":10}

print(dict1)

print(len(dict1))  #4

#print value in the dictionary with specific key

print(dict1[1])   #pranav

print("Add new key value in the dictionary")
dict1[5]="Rinisha"
print(dict1)

print("update/modify value in the dictionary for specific key")

dict1[1]="pranav uttarwar"
print(dict1)

print("delete k-v paire from the dictionary")

dict1.pop(3)
print(dict1)

print("delete k-v pair from last position in the dictionary")

dict1.popitem()
print(dict1)

print("check key exist in the dictionary")
print('Papa' in dict1) #true and false output


print("----All keys only  in the dictionary----")
allkeys=dict1.keys()

for i in allkeys:
    print(i)

print("-----All Values only in the dictionary-----")

allValues = dict1.values()

for i in allValues:
    print(i)

print("-----Get all Key - Values pairs in the dictionary-----")
allkeyValue=dict1.items()

for key,value in allkeyValue:
    print(key, ",", value)

